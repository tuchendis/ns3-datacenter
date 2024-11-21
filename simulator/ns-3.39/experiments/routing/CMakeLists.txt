build_experiment(
  NAME fattree-with-global-routing
  SOURCE_FILES 
    fattree-with-global-routing.cc
  HEADER_FILES
  LIBRARIES_TO_LINK
    ${libpoint-to-point}
    ${libtraffic-control}
    ${libinternet}
    ${libapplications}
)