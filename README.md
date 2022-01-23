# Boston-Route-Planner
About A route planner using the A*, dijkstra and bellman-ford algorithm (uses Open Street Map data)
### Abstract

This project aims to the development of a visual and interactive Boston navigation map application. The app can find the shortest path and its distance according to the departure point and destination point you provide. You can choose to use different search algorithms (Dijkstra’s, Bellman-Ford with a Queue and A* with a heap) to find the shortest path. The results have been tested to be correct and displayed on the interactive map in the web page.

### Instruction

Running files in Linux system with Python 3.8

1. Install geopy, flask(1.1.2), heapdict by the following commands:

   `pip install geopy`

   `pip install flask`

   `Pipinstall heapdict`

2. Run the code

   In the project folder(the same path as flask_map.py):

   `python flask_map.py`

 

3.  Enter the website

   There are two ways to access the web application

   - Ctrl + click the website shown in the terminal.

   - Open 127.0.0.1:60000 in Web Browser

![clip_image002](https://user-images.githubusercontent.com/90360797/150661339-56998cb9-e53d-49d8-b9a0-2e7179276360.jpg)


4. How to use Boston Navigation System?

   - Drag the cursor to find the latitude and longitude of departure point.

   - Copy the latitude and longitude into the departure input box.

   -  Again, drag the cursor to find the latitude and longitude of destination point.

   - Copy the latitude and longitude into the destination input box.

   - Choose the algorithm by inputting A (A*), B (Bellman-Ford) or D (Dijkstra). 

   - Click ‘Navigation’ button.

   - The shortest path and its distance will be shown on the map. You can zoom in and zoom out the map by mouse wheel.

![clip_image004](https://user-images.githubusercontent.com/90360797/150661343-a345331a-f4fc-4a31-9570-3a546201e3d6.png)

![clip_image006](https://user-images.githubusercontent.com/90360797/150661347-8af236b6-23f5-432b-879d-d6b4220d7761.png)


###  Sample Results

In order to test the correctness of the three algorithms, we use the two nodes as the starting point and the ending point, and use the three algorithms to calculate the shortest path.

We test the program by giving node ‘61324188’ ([42.3705222, -71.0755329]) as the source and ‘61327443’ ([42.3657096, -71.0767703]) as the destination. As we can see from the result, it prints out nodes the shortest path should pass through and the distance between the source and the destination. Such distance is computed by geopy.distance.

![clip_image008](https://user-images.githubusercontent.com/90360797/150661349-dbd11aad-5ec6-4fa0-aa70-8263aa7b0c4f.png)


From the figure above, we can see that the path and the shortest distance obtained by the three algorithms are the same, so we can confirm the correctness of the three algorithms.
 

In the Boston Navigation System, we randomly choose two points as the starting point and the ending point and use Bellman-Ford algorithm to find the shortest path between them.

![clip_image010](https://user-images.githubusercontent.com/90360797/150661354-331a64db-6467-407d-b08c-9c348402e429.png)


The result is shown in the figure below

![clip_image012](https://user-images.githubusercontent.com/90360797/150661356-48d49458-89b2-4145-8c67-c3f8f8e953c5.png)

Using A* algorithm to test the other two points, the result is as follows.

![clip_image014](https://user-images.githubusercontent.com/90360797/150661358-d10381ea-c42a-4c20-8a41-645073b93772.jpg)


### References

[1]https://blog.csdn.net/hju22/article/details/85111071?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-15.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-15.control

[2]https://automating-gis-processes.github.io/CSC18/lessons/L3/retrieve-osm-data.html

[3]https://gist.github.com/rajanski/2e7d3df6654ce6d96afb

[4]https://gis.stackexchange.com/questions/180543/osm2po-postgres-to-graph-for-a

[5]https://www.educative.io/edpresso/how-to-implement-dijkstras-algorithm-in-python

 
