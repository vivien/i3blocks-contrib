#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <getopt.h>

#define RED "#FF7373"
#define ORANGE "#FFA500"

typedef unsigned long long int ulli;

enum {
  STATE_OK,
  STATE_WARNING,
  STATE_CRITICAL,
  STATE_UNKNOWN,
};

void usage(char *argv[])
{
  printf("Usage: %s [-b|B] [-t seconds] [-i interface] [-w Bytes:Bytes] [-c Bytes:Bytes] [-h]\n", argv[0]);
  printf("\n");
  printf("-b \t\tuse bits/s\n");
  printf("-B \t\tuse Bytes/s  (default)\n");
  printf("-t seconds\trefresh time (default is 1)\n");
  printf("-i interface\tnetwork interface to monitor. If not specified, check all interfaces.\n");
  printf("-w Bytes:Bytes\tSet warning (color orange) for Rx:Tx bandwidth. (default: none)\n");
  printf("-c Bytes:Bytes\tSet critical (color red) for Rx:Tx bandwidth. (default: none)\n");
  printf("-h \t\tthis help\n");
  printf("\n");
}

void get_values(char *const iface, time_t * const s, ulli * const received, ulli * const sent)
{
  FILE *f;

  f = fopen("/proc/net/dev", "r");
  if (!f) {
    fprintf(stderr, "Can't open /proc/net/dev\n");
    exit(STATE_UNKNOWN);
  }

  ulli temp_r, temp_s;
  char line[BUFSIZ];
  char ifname[BUFSIZ];

  *received = 0;
  *sent = 0;
  while (fgets(line, BUFSIZ - 1, f) != NULL) {
    if (sscanf(line, "%s %llu %*u %*u %*u %*u %*u %*u %*u %llu", ifname, &temp_r, &temp_s) == 3) {
      if (iface && strcmp(iface, ifname) != 0) {
        continue;
      }

      if (strcmp(ifname, "lo:") == 0)
        continue;

      *received = *received + temp_r;
      *sent = *sent + temp_s;
    }
  }

  fclose(f);

  *s = time(NULL);
  if (!s) {
    fprintf(stderr, "Can't get Epoch time\n");
    exit(STATE_UNKNOWN);
  }
}

void display(int const unit, double b, int const warning, int const critical)
{
  if (critical != 0 && b > critical) {
    printf("<span color='%s'>", RED);
  } else if (warning != 0 && b > warning) {
    printf("<span color='%s'>", ORANGE);
  } else {
    printf("<span>");
  }

  if (unit == 'b')
    b = b * 8;

  if (b < 1024) {
    printf("%5.1lf  %c/s", b, unit);
  } else if (b < 1024 * 1024) {
    printf("%5.1lf K%c/s", b / 1024, unit);
  } else if (b < 1024 * 1024 * 1024) {
    printf("%5.1lf M%c/s", b / (1024 * 1024), unit);
  } else {
    printf("%5.1lf G%c/s", b / (1024 * 1024 * 1024), unit);
  }
  printf("</span>");
}

int main(int argc, char *argv[])
{
  int c, unit = 'B', t = 1;
  char *iface = NULL;
  int warningrx = 0, warningtx = 0, criticalrx = 0, criticaltx = 0;
  while (c = getopt(argc, argv, "bBht:i:w:c:"), c != -1) {
    switch (c) {
    case 'b':
    case 'B':
      unit = c;
      break;
    case 't':
      t = atoi(optarg);
      break;
    case 'i':
      iface = strcat(optarg, ":");
      break;
    case 'w':
      sscanf(optarg, "%d:%d", &warningrx, &warningtx);
      break;
    case 'c':
      sscanf(optarg, "%d:%d", &criticalrx, &criticaltx);
      break;
    case 'h':
      usage(argv);
      return STATE_UNKNOWN;
    }
  }

  time_t s, s_old;
  ulli received, sent, received_old, sent_old;
  double rx, tx;

  get_values(iface, &s_old, &received_old, &sent_old);

  while (1) {
    sleep(t);
    get_values(iface, &s, &received, &sent);

    rx = (received - received_old) / (float)(s - s_old);
    tx = (sent - sent_old) / (float)(s - s_old);
    display(unit, rx, warningrx, criticalrx);
    printf(" ");
    display(unit, tx, warningtx, criticaltx);
    fflush(stdout);
    s_old = s;
    received_old = received;
    sent_old = sent;
  }

  return STATE_OK;
}
