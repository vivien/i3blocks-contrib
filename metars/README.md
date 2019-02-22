The purpose of *metars* script is to deliver reliable weather information. According to Wikipedia METAR weather report is "predominantly used by pilots in fulfillment of a part of a pre-flight weather briefing, and by meteorologists, who use aggregated METAR information to assist in weather forecasting." In addition to showing data directly from a METAR station this script also displays "feels like" (wind chill) temperature for static winds and gusts as explained in the [Wind chill](https://en.wikipedia.org/wiki/Wind_chill) Wikipedia article ("The standard wind chill formula").

METAR stations are typically located at airports and defined by four-letter station codes. The four-letter METAR station data is based on ICAO codes and locations along with their codes can be found in the [ICAO airport code](https://en.wikipedia.org/wiki/ICAO_airport_code) Wikipedia article.

# Configuration

The shown weather is in *MetarsConfig* and examples are in commented out sections under "metric config" and "imperial config." Only *MetarsConfig* should be edited to match the "metric config" or "imperial config" sections, however any combination of custom configurations is possible.

*MetarsEnablements* configures what is shown on the status line. Some information may be optional and some required based only individual needs and available spaces for the status bar. Some options are currently not implemented. These include weather forecasts and rainfall.

The used weather station is received either from the *METARSTATION* environment variable or it can be configured directly in the fallback configuration (currently *EFHK* in the script file) if the environment variable is missing.

Wind direction: The flag *useInverseDirIcons* refers to how the wind direction icon is displayed. The "default" behavior is to show the traditional "finger" style ("useInverseDirIcons=false"), i.e. if the wind is blowing from south to north the finger points to south. The purpose of the "useInverseDirIcons=true" is to show direction of the wind, i.e. an arrow from south to north is shown (pointing to north). The safest option is to leave this setting as "false" so that it follows the official wind direction measurement style (described in [Wind direction](https://en.wikipedia.org/wiki/Wind_direction) and [Wind vane](https://en.wikipedia.org/wiki/Weather_vane) Wikipedia articles).

Note: If the wind direction is missing it is usually because the wind direction data is either missing or is marked as "variable", i.e. there are many values for the wind's direction inside a certain measurement time window.

# Behavior

Clicking the *metars* status line causes the status line to be updated and raw METAR updated status to be displayed with *libnotify* (*notify-send*). This behavior requires *libnotify* package to be installed, possibly also package *dunst* or any other similar option. The title bar clicking behavior reacts to left, middle and right buttons but may be configured to any number of buttons. The most essential package for this script is the *python-metar* package, installed with "python pip python-metar".

