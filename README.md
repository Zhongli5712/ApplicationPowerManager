# ApplicationPowerManager

---
## Introduction
Wanting to find out how much power does a program need to run?

Current tools such as Intel Power Gadget only measure the power usage or your computer, but not your program.
ApplicationPowerManager solves your problem by allowing you to estimate the power usage of one application.

---
## Acknowledgement

ApplicationPowerManager use `EnergyLib64.dll` provided by [Intel Power Gadget](https://www.intel.com/content/www/us/en/developer/articles/tool/power-gadget.html).

---
## Setting up and getting started

### Setting up
1. Make sure you have `Python` version 3.8 or later installed.
2. Download the zip file in the [latest release](https://github.com/Zhongli5712/ApplicationPowerManager/releases) into a new folder, unzip it and run `ApplicationPowerManager.py` to run the ApplicationPowerManager
   1. One way to run is open terminal at current folder, run using command `python ApplicationPowerManager.py`

### Using the application
1. Upon running the ApplicationPowerManager, you will see the message `Please wait a moment...`.
2. After a few seconds, a new message will appear `Now run the application you want to measure the power usage.` and a confirmation is required `Have you run it? (yes/no)`
3. Now you need to run the application you want to measure.
4. Confirming your application is running by replying `yes`
5. Wait and see the result.
---
## Design

### Overview

ApplicationPowerManager retrieves and calculates difference of power usage before and after you run the application you want to measure and output the estimation of power usage required.

### Implementation
#### init:
Load the Intel Power Gadget library `EnergyLib64.dll` and initialize it.

#### generate_report:
Use API from `EnergyLib64.dll` to measure the average power usage when calling `ReadSample()` and save into specified `csv` file.

#### main:
1. Before you run the application you want to measure, measure the power usage and save into `PowerGadgetLogBefore.csv`.
2. After confirming you have run the application you want to measure, measure the power usage again and save into `PowerGadgetLogAfter.csv`.
3. Retrieving the `Average Processer Power` and calculate the difference.
   1. Result output might be a message that says the result is 0 or there is an error somewhere. You need to run the application again.
---
## Current drawbacks

1. ApplicationPowerManager only provides the estimation, and may generate different result if there is a background application that end or start during measuring and logging `PowerGadgetLogAfter.csv`, so multiple try should be done to obtain the closet estimation (run the ApplicationPowerManager multiple time and record the result, afterwards decide the closet estimation).
   - For example after running ApplicationPowerManager multiple times and obtains results `2.23, 1.97, 2.4, 5.52, 0.99` we can see that the estimation would be around `2.2` with values `5.52` and `0.99` be the outliner.
2. Result output might be a message that says the result is 0 or there is an error somewhere, it might be caused by another application using a greater amount of power end during the estimating. You have to run the application again in this case.
---
## Difficulties during implementation

- The documentation for Intel Power Gadget API is not well maintained, some files are missing.
- There are not many other tools that offer developer API.
