---
UID : NS:gnssdriver.GNSS_SELFTESTRESULT
title : GNSS_SELFTESTRESULT
author : windows-driver-content
description : This structure defines the specific data elements associated with a carrier wave test results returned from the driver.
old-location : sensors\gnss_selftestresult.htm
old-project : sensors
ms.assetid : 572A2C38-A990-4225-A3FC-6E899A248B1C
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : GNSS_SELFTESTRESULT, *PGNSS_SELFTESTRESULT, GNSS_SELFTESTRESULT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : gnssdriver.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : GNSS_SELFTESTRESULT
req.alt-loc : gnssdriver.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PGNSS_SELFTESTRESULT, GNSS_SELFTESTRESULT"
---

# GNSS_SELFTESTRESULT structure
This structure defines the specific data elements associated with a carrier wave test results returned from the driver.

## Syntax
````
typedef struct {
  ULONG    Size;
  ULONG    Version;
  NTSTATUS TestResultStatus;
  ULONG    Result;
  ULONG    PinFailedBitMask;
  BYTE     Unused[512];
  ULONG    OutBufLen;
  BYTE     OutBuffer[BYTE];
} GNSS_SELFTESTRESULT, *PGNSS_SELFTESTRESULT;
````

## Members

        
            `OutBufLen`

            The length of the buffer for returning any additional information about the self-test.
        
            `PinFailedBitMask`

            The bit mask for adapter pins that failed the test.
        
            `Result`

            The final result of the self-test.
        
            `Size`

            Structure size.
        
            `TestResultStatus`

            NTSTATUS value indicating:

<ul>
<li>
Success (self-test passed).

</li>
<li>
Failed (indicating the problem detected or indicating that the is test not implemented).

</li>
</ul>
        
            `Version`

            Version number.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | gnssdriver.h |