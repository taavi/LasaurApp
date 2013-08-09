


Speed Optimization
-------------------

- running python backend/test_svg.py -p
- 33% in find_cut_settings_tags
- 50% in regex parsing in svg_tag_reader
- 16% in simplify



rocket.svg
-----------
         697607 function calls (671857 primitive calls) in 3.256 seconds

   Ordered by: cumulative time
   List reduced from 148 to 40 due to restriction <40>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.256    3.256 profile:0(main())
        1    0.000    0.000    3.256    3.256 <string>:1(<module>)
        1    0.004    0.004    3.256    3.256 /home/noema/Development/git/LasaurApp/backend/filereaders/__init__.py:14(read_svg)
        1    0.000    0.000    3.256    3.256 backend/test_svg.py:36(main)
        1    0.000    0.000    2.816    2.816 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:100(parse)
   2396/1    0.116    0.000    2.788    2.788 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:242(parse_children)
     2395    0.108    0.000    2.572    0.001 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:41(read_tag)
33343/14231    0.240    0.000    1.640    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:51(read_attrib)
     2389    0.228    0.000    0.732    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:158(styleAttrib)
     2351    0.052    0.000    0.580    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:139(line)
     9404    0.032    0.000    0.572    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:76(dimensionAttrib)
     9404    0.140    0.000    0.540    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:203(_parseUnit)
     2351    0.116    0.000    0.472    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:28(add_path)
    40432    0.184    0.000    0.444    0.000 /usr/lib/python2.7/logging/__init__.py:1118(debug)
        1    0.000    0.000    0.436    0.436 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:197(optimize_all)
       61    0.004    0.000    0.412    0.007 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:52(simplify)
        1    0.000    0.000    0.412    0.412 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:157(simplify_all)
  4253/61    0.160    0.000    0.380    0.006 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:76(simplifyDP)
     9447    0.084    0.000    0.316    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/utilities.py:6(parseFloats)
    40435    0.168    0.000    0.260    0.000 /usr/lib/python2.7/logging/__init__.py:1332(isEnabledFor)
    14118    0.148    0.000    0.208    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:73(d2)
     9490    0.096    0.000    0.200    0.000 /usr/lib/python2.7/re.py:169(findall)
     9404    0.116    0.000    0.180    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:53(_nextIsNum)
     4778    0.044    0.000    0.152    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:80(colorAttrib)
76200/76189    0.132    0.000    0.132    0.000 :0(len)
    16457    0.104    0.000    0.116    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:61(_getNext)
     4778    0.036    0.000    0.108    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:226(_parseColor)
    73804    0.108    0.000    0.108    0.000 :0(strip)
    40435    0.092    0.000    0.092    0.000 /usr/lib/python2.7/logging/__init__.py:1318(getEffectiveLevel)
    52175    0.072    0.000    0.072    0.000 :0(get)
     4804    0.032    0.000    0.056    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:245(_get_tag)
     9490    0.048    0.000    0.052    0.000 /usr/lib/python2.7/re.py:226(_compile)
     9490    0.052    0.000    0.052    0.000 :0(findall)
    28134    0.048    0.000    0.048    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:68(diff)
    18855    0.044    0.000    0.044    0.000 :0(range)
     2389    0.028    0.000    0.044    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/webcolors.py:404(normalize_hex)
     2351    0.020    0.000    0.040    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:251(_has_valid_stroke)
    18813    0.040    0.000    0.040    0.000 :0(endswith)
    21501    0.040    0.000    0.040    0.000 :0(split)
     2351    0.036    0.000    0.040    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:35(_matrixExtractScale)



full-bed.svg
-------------

         3359572 function calls (3271750 primitive calls) in 18.121 seconds

   Ordered by: cumulative time
   List reduced from 156 to 40 due to restriction <40>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   18.121   18.121 profile:0(main())
        1    0.004    0.004   18.121   18.121 <string>:1(<module>)
        1    0.000    0.000   18.117   18.117 backend/test_svg.py:36(main)
        1    0.004    0.004   18.109   18.109 /home/noema/Development/git/LasaurApp/backend/filereaders/__init__.py:14(read_svg)
        1    0.000    0.000   12.917   12.917 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:100(parse)
  14134/1    0.808    0.000   12.841   12.841 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:242(parse_children)
    14133    0.616    0.000   11.169    0.001 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:41(read_tag)
    14096    0.188    0.000    5.332    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:83(path)
        1    0.000    0.000    5.188    5.188 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:197(optimize_all)
        1    0.012    0.012    4.856    4.856 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:157(simplify_all)
      840    0.224    0.000    4.840    0.006 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:52(simplify)
    14096    0.700    0.000    4.512    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:28(add_path)
82866/54672    0.768    0.000    4.272    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:51(read_attrib)
26600/840    1.448    0.000    4.060    0.005 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:76(simplifyDP)
    14097    0.516    0.000    2.532    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:158(styleAttrib)
   191136    1.164    0.000    2.056    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:73(d2)
     1184    0.076    0.000    1.976    0.002 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:375(addArc)
20832/1184    0.624    0.000    1.812    0.002 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:420(_recursiveArc)
   153516    0.712    0.000    1.728    0.000 /usr/lib/python2.7/logging/__init__.py:1118(debug)
   153520    0.720    0.000    1.016    0.000 /usr/lib/python2.7/logging/__init__.py:1332(isEnabledFor)
    28193    0.152    0.000    0.968    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:80(colorAttrib)
   370416    0.936    0.000    0.936    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:68(diff)
    64864    0.548    0.000    0.904    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:413(_getVertex)
    28193    0.256    0.000    0.816    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:226(_parseColor)
    29680    0.412    0.000    0.780    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:53(_nextIsNum)
    92752    0.480    0.000    0.668    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:61(_getNext)
    14096    0.256    0.000    0.628    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:179(dAttrib)
   225875    0.592    0.000    0.592    0.000 :0(get)
    14096    0.300    0.000    0.588    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:251(_has_valid_stroke)
222314/222294    0.584    0.000    0.584    0.000 :0(len)
   216464    0.484    0.000    0.484    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:71(norm2)
   127879    0.428    0.000    0.428    0.000 :0(append)
    14097    0.216    0.000    0.416    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/webcolors.py:404(normalize_hex)
   153952    0.404    0.000    0.404    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:70(dot)
   155113    0.312    0.000    0.312    0.000 :0(strip)
    14120    0.072    0.000    0.304    0.000 /usr/lib/python2.7/re.py:169(findall)
   153520    0.296    0.000    0.296    0.000 /usr/lib/python2.7/logging/__init__.py:1318(getEffectiveLevel)
        1    0.260    0.260    0.264    0.264 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:172(sort_by_seektime)
    66048    0.216    0.000    0.216    0.000 :0(cos)
    14096    0.128    0.000    0.200    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:35(_matrixExtractScale)




Steven and Chris Picture Frame - with ERROR.svg
-----------------------------------------------

         907762 function calls (896618 primitive calls) in 49.239 seconds

   Ordered by: cumulative time
   List reduced from 151 to 40 due to restriction <40>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   49.239   49.239 profile:0(main())
        1    0.004    0.004   49.239   49.239 <string>:1(<module>)
        1    0.000    0.000   49.235   49.235 /home/noema/Development/git/LasaurApp/backend/filereaders/__init__.py:14(read_svg)
        1    0.000    0.000   49.235   49.235 backend/test_svg.py:36(main)
        1    0.000    0.000   46.663   46.663 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:197(optimize_all)
        2   44.923   22.461   44.983   22.491 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:172(sort_by_seektime)
        1    0.000    0.000    2.548    2.548 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:102(parse)
     50/1    0.160    0.003    2.544    2.544 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:244(parse_children)
       49    0.000    0.000    2.260    0.046 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:43(read_tag)
       42    0.000    0.000    2.180    0.052 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:85(path)
       42    0.380    0.009    2.180    0.052 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:28(add_path)
        2    0.108    0.054    1.632    0.816 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:157(simplify_all)
     9888    0.304    0.000    1.468    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:52(simplify)
    41645    0.524    0.000    0.996    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:53(_nextIsNum)
14204/9888    0.312    0.000    0.840    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:76(simplifyDP)
    54223    0.316    0.000    0.544    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:73(d2)
    68221    0.324    0.000    0.492    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:61(_getNext)
208242/208212    0.484    0.000    0.484    0.000 :0(len)
   105111    0.268    0.000    0.268    0.000 :0(append)
7597/1235    0.160    0.000    0.216    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_path_reader.py:300(addCubicBezier)
    89475    0.196    0.000    0.196    0.000 :0(isinstance)
    95288    0.168    0.000    0.168    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:68(diff)
    58382    0.152    0.000    0.152    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:71(norm2)
    41717    0.104    0.000    0.104    0.000 :0(range)
  407/143    0.000    0.000    0.076    0.001 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:54(read_attrib)
    36906    0.072    0.000    0.072    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:70(dot)
       42    0.036    0.001    0.072    0.002 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:182(dAttrib)
    27205    0.060    0.000    0.060    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/utilities.py:28(matrixApply)
    15194    0.052    0.000    0.052    0.000 :0(abs)
        2    0.020    0.010    0.048    0.024 /home/noema/Development/git/LasaurApp/backend/filereaders/path_optimizers.py:24(join_segments)
    27205    0.044    0.000    0.044    0.000 /home/noema/Development/git/LasaurApp/backend/filereaders/utilities.py:34(vertexScale)
       48    0.036    0.001    0.036    0.001 :0(findall)
        3    0.004    0.001    0.024    0.008 /usr/lib/python2.7/re.py:226(_compile)
        1    0.000    0.000    0.024    0.024 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_tag_reader.py:18(__init__)
        1    0.000    0.000    0.024    0.024 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_reader.py:68(__init__)
        3    0.000    0.000    0.024    0.008 /usr/lib/python2.7/re.py:188(compile)
        3    0.000    0.000    0.020    0.007 /usr/lib/python2.7/sre_compile.py:495(compile)
        1    0.000    0.000    0.012    0.012 /home/noema/Development/git/LasaurApp/backend/filereaders/svg_attribute_reader.py:17(__init__)
        3    0.000    0.000    0.012    0.004 /usr/lib/python2.7/sre_compile.py:480(_code)
     48/3    0.004    0.000    0.012    0.004 /usr/lib/python2.7/sre_compile.py:32(_compile)
