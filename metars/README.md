# Introduction

The purpose of *metars* script is to deliver reliable weather information. According to Wikipedia METAR weather report (METeorological Aerodrome Report) is "predominantly used by pilots in fulfillment of a part of a pre-flight weather briefing, and by meteorologists, who use aggregated METAR information to assist in weather forecasting." In addition to showing data directly from a METAR station this script also displays "feels like" (wind chill) temperature for static winds and gusts as explained in the [Wind chill](https://en.wikipedia.org/wiki/Wind_chill) Wikipedia article ("The standard wind chill formula").

METAR weather stations are typically located at airports and defined by four-letter station codes. The four-letter METAR station data is based on ICAO codes and locations along with their codes can be found in the [ICAO airport code](https://en.wikipedia.org/wiki/ICAO_airport_code) Wikipedia article.

# i3blocks configuration

Configuration sample:

```
[metars]
interval=2100
METARSSTATION=EFHK
METARSURL=https://tgftp.nws.noaa.gov/data/observations/metar/stations/{}.TXT
METARSENABLEMENTS={ "temperature": true, "dewpoint" : false, "feelsLike" : true, "wind" : true, "pressure" : false, "visibility" : false, "windDirType" : "icon", "useInverseWind" : false }
METARSCONFIGS={ "temperatureUnit" : "C", "temperatureSym" : "°C", "pressureUnit" : "HPA", "pressureSym" : "hPa", "speedUnit" : "MPS", "speedSym" : "m/s", "distanceUnit" : "KM", "distanceSym" : "km", "precipitationUnit" : "CM", "precipitationSym" : "cm"}
```
## Configuration option *interval*

METAR stations are usually updated every 30 or 60 minutes. This example specifies 2100 seconds (35 minutes).

## Configuration option *METARSSTATION*

This is the four-letter ICAO airport code. It will be used as part of *METARSURL*.

## Configuration option *METARSURL*

This URL is used when fetching the METAR weather data. This string must include "{}", replaced by the script with *METARSSTATION*.

## Configuration option *METARSENABLEMENTS*

These options specify what information is shown on the line. This is a JSON string and each key and value needs to be inside double quotes except for booleans that need to be specified with lower case "true" and "false".

## Configuration option *METARSENABLEMENTS/temperature*

This option commands the temperature information to be shown.

## Configuration option *METARSENABLEMENTS/dewpoint*

This option commands the [dew point](https://en.wikipedia.org/wiki/Dew_point) information to be shown.

## Configuration option *METARSENABLEMENTS/feelsLike*

This option commands the [wind chill](https://en.wikipedia.org/wiki/Wind_chill) information to be shown.

## Configuration option *METARSENABLEMENTS/wind*

This option commands the wind information, both static and gusts along with their direction to be shown.

## Configuration option *METARSENABLEMENTS/visibility*

This option commands the visibility to be shown. Visibility is diminished during bad weather conditions and over 10 kilometer visibility is usually described as "10 km".

## Configuration option *METARSENABLEMENTS/windDirType*

This option specifies the wind direction type. Three options are supported. Option *angle* commands the direction to be shown as angles in clockwise direction. Option *text* commands the direction to be shown as 1 to 3 letter [compass style letters](https://en.wikipedia.org/wiki/Points_of_the_compass). Option *icon* commands the direction to be shown as graphical arrow arrow symbol.

## Configuration option *METARSENABLEMENTS/useInverseWind*

This option modifies the behavior of the *windDirType* option by rotating the direction 180 degrees. The safest option is to leave this setting as *false* so that it follows the official wind direction measurement style (described in [Wind direction](https://en.wikipedia.org/wiki/Wind_direction) and [Wind vane](https://en.wikipedia.org/wiki/Weather_vane) Wikipedia articles). If this option is *false* its meaning is "wind is from that direction", if it is *true* its meaning is "wind is to that direction". Inverse wind direction is sometimes used in graphical notation where the arrow represents the wind itself.

## Configuration option *METARSCONFIGS*

These options specify the fine tuning of elements set as visible with the *METARSENABLEMENTS* options. This is a JSON string and each key and value needs to be inside double quotes except for booleans that need to be specified with lower case "true" and "false".

## Configuration option *METARSCONFIGS/temperatureUnit*

This option specifies the [temperature unit](https://github.com/python-metar/python-metar/blob/master/metar/Datatypes.py) of *python-metar*. Currently supported values are *F* (Fahrenheit), *C* (Celcius) and *K* (Kelvin).

## Configuration option *METARSCONFIGS/temperatureSym*

This option specifies the type of symbol or text to be shown on the line after the temperature value.

## Configuration option *METARSCONFIG/pressureUnit*

This option specifies the [barometric pressure unit](https://github.com/python-metar/python-metar/blob/master/metar/Datatypes.py) of *python-metar*. Currently supported values are *MB* (millibar), *HPA* (hectopascal) and *IN* (inch of mercury).

## Configuration option *METARSCONFIG/pressureSym*

This option specifies the type of symbol or text to be shown on the line after the barometric pressure value.

## Configuration option *METARSCONFIG/speedUnit*

This option specifies the [speed unit](https://github.com/python-metar/python-metar/blob/master/metar/Datatypes.py) of *python-metar*. Currently supported values are *KT* (knots), *MPS* (meters per second), *KMH* (kilometers per hour) and *MPH* (miles per hour).

## Configuration option *METARSCONFIG/speedSym*

This option specifies the type of symbol or text to be shown on the line after the speed value.

## Configuration option *METARSCONFIG/distanceUnit*

This option specifies the [distance unit](https://github.com/python-metar/python-metar/blob/master/metar/Datatypes.py) of *python-metar*. Currently supported values are *SM* (miles), *MI* (miles), *M* (meters), *KM* (kilometers), *FT* (feet) and *IN* (inches).

## Configuration option *METARSCONFIG/distanceSym*

This option specifies the type of symbol or text to be shown on the line after the distance value.

## Configuration option *METARSCONFIG/precipitationUnit*

This option specifies the [precipitation unit](https://github.com/python-metar/python-metar/blob/master/metar/Datatypes.py) of *python-metar*. Currently supported values are "IN" (inches) and "CM" (centimeters).

## Configuration option *METARSCONFIG/precipitationSym*

This option specifies the type of symbol or text to be shown on the line after the precipitation value.

## Other configuration options

Other related options are *command* and *separator_block_width* but these can be defined outside the blocklets.

# Behavior

Clicking the *metars* status line causes the status line to be updated and raw METAR updated status to be displayed with *libnotify* (*notify-send*). This behavior requires *libnotify* package to be installed, possibly also package *dunst* or any other similar option. The title bar clicking behavior reacts to left, middle and right buttons but may be configured to any number of buttons. The most essential package for this script is the *python-metar* package, installed with "python pip python-metar".

