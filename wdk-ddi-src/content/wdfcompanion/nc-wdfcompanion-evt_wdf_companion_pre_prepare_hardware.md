---
UID: NC:wdfcompanion.EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE
title: EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE
author: windows-driver-content
description: For internal use only.
old-location: wdf\evt_wdf_companion_pre_prepare_hardware.htm
old-project: wdf
ms.assetid: 36076a28-d3f7-4463-b538-59794a18c4f9
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.evt_wdf_companion_pre_prepare_hardware, EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE callback function, EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE, EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE, EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE, wdfcompanion/EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	wdfcompanion.h
apiname:
-	EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE
product: Windows
targetos: Windows
req.typenames: "*PWDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG"
req.product: Windows 10 or later.
---


# EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE function
For internal use only.

## Syntax

```
EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE EvtWdfCompanionPrePrepareHardware;

NTSTATUS EvtWdfCompanionPrePrepareHardware(
  WDFCOMPANION Companion,
  WDFCMRESLIST ResourcesRaw,
  WDFCMRESLIST ResourcesTranslated
)
{...}
```

## Parameters

`Companion`



`ResourcesRaw`



`ResourcesTranslated`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Minimum UMDF version** | 2.23 |
| **Header** | wdfcompanion.h |
| **IRQL** | PASSIVE_LEVEL |