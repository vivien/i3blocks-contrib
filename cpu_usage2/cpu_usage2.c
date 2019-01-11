// Licensed under the terms of the GNU GPL v3, or any later version.
//
// Copyright 2019 Nolan Leake <nolan@sigbus.net>
//
// Loosely based on bandwidth2 (originally by Guillaume Coré <fridim@onfi.re>)

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>

#define RED "#FF7373"
#define ORANGE "#FFA500"

typedef unsigned long long int ulli;

void usage(char *argv[])
{
  printf("Usage: %s "
         "[-t seconds] [-w %%age] [-c %%age] [-d decimals] [-l label] [-h]\n",
         argv[0]);
  printf("\n");
  printf("-t seconds\trefresh time (default is 1)\n");
  printf("-w %%\tSet warning (color orange) for cpu usage. (default: none)\n");
  printf("-c %%\tSet critical (color red) for cpu usage. (default: none)\n");
  printf("-d number\tNumber of decimal places for percentage (default: 2)\n");
  printf("-l label\tLabel to print before the cpu usage (default: CPU)\n");
  printf("-h \t\tthis help\n");
  printf("\n");
}

void display(const char *label, double used,
             int const warning, int const critical, int const decimals)
{
  if (critical != 0 && used > critical) {
    printf("%s<span color='%s'>", label, RED);
  } else if (warning != 0 && used > warning) {
    printf("%s<span color='%s'>", label, ORANGE);
  } else {
    printf("%s<span>", label);
  }

  printf("%*.*lf%%</span>\n", decimals + 3 + 1, decimals, used);
}

ulli get_usage(ulli *used_jiffies)
{
  FILE *fd = fopen("/proc/stat", "r");
  ulli user, nice, sys, idle, iowait, irq, sirq, steal, guest, nguest;

  if (!fd) {
    perror("Couldn't open /proc/stat\n");
    exit(EXIT_FAILURE);
  }
  if (fscanf(fd, "cpu  %llu %llu %llu %llu %llu %llu %llu %llu %llu %llu",
             &user, &nice, &sys, &idle, &iowait, &irq, &sirq,
             &steal, &guest, &nguest) != 10) {
    perror("Couldn't read jiffies from /proc/stat\n");
    exit(EXIT_FAILURE);
  }
  fclose(fd);

  *used_jiffies = user + nice + sys + irq + sirq + steal + guest + nguest;
  return *used_jiffies + idle + iowait;
}

int main(int argc, char *argv[])
{
  int warning = 50, critical = 80, t = 1, decimals = 2;
  char *label = "CPU ";
  int c;
  char *envvar = NULL;

  envvar = getenv("REFRESH_TIME");
  if (envvar)
    t = atoi(envvar);
  envvar = getenv("WARN_PERCENT");
  if (envvar)
    warning = atoi(envvar);
  envvar = getenv("CRIT_PERCENT");
  if (envvar)
    critical = atoi(envvar);
  envvar = getenv("DECIMALS");
  if (envvar)
    decimals = atoi(envvar);
  envvar = getenv("LABEL");
  if (envvar)
    label = envvar;

  while (c = getopt(argc, argv, "ht:w:c:d:l:"), c != -1) {
    switch (c) {
    case 't':
      t = atoi(optarg);
      break;
    case 'w':
      warning = atoi(optarg);
      break;
    case 'c':
      critical = atoi(optarg);
      break;
    case 'd':
      decimals = atoi(optarg);
      break;
    case 'l':
      label = optarg;
      break;
    case 'h':
      usage(argv);
      return EXIT_SUCCESS;
    }
  }

  ulli old_total;
  ulli old_used;

  old_total = get_usage(&old_used);

  while (1) {
    ulli used;
    ulli total;

    sleep(t);
    total = get_usage(&used);

    display(label, 100.0D * (used - old_used) / (total - old_total),
            warning, critical, decimals);
    fflush(stdout);
    old_total = total;
    old_used = used;
  }

  return EXIT_SUCCESS;
}
