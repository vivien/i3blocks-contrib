#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

long getFreeRam()
{
    FILE *fpipe;
    char *command = "grep MemAvailable /proc/meminfo";
    char c = 0;

    if (0 == (fpipe = (FILE*)popen(command, "r")))
    {
        perror("popen() failed.");
        exit(EXIT_FAILURE);
    }
    
    char textValue[30];

    int count = 0;
    while (fread(&c, sizeof c, 1, fpipe))
    {
        if(c >= '0' && c <= '9'){
            textValue[count] = c;
            count++;
        }
    }
    textValue[count] = '\0';

    pclose(fpipe);

    long result = atol(textValue);

    return result;

}

long getTotalRam()
{
    FILE *fpipe;
    char *command = "grep MemTotal /proc/meminfo";
    char c = 0;

    if (0 == (fpipe = (FILE*)popen(command, "r")))
    {
        perror("popen() failed.");
        exit(EXIT_FAILURE);
    }
    
    char textValue[30];

    int count = 0;
    while (fread(&c, sizeof c, 1, fpipe))
    {
        if(c >= '0' && c <= '9'){
            textValue[count] = c;
            count++;
        }
    }
    textValue[count] = '\0';

    pclose(fpipe);

    long result = atol(textValue);

    return result;

}