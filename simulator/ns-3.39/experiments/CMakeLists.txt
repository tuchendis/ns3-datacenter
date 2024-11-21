subdirlist(experiments_to_build ${CMAKE_CURRENT_SOURCE_DIR})

# Process subdirectories
foreach(experimentfolder ${experiments_to_build})
  if(NOT (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${experiments_to_build}/CMakeLists.txt))
    continue()
  endif()
  add_subdirectory(${experiments_to_build})

  set(ns3-experiment-folders
      "${experimentfolder};${ns3-experiment-folders}"
      CACHE INTERNAL "list of experiment folders"
  )
endforeach()