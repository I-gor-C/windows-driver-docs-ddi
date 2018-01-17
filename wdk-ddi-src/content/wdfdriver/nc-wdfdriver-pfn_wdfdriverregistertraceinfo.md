---
UID: NC:wdfdriver.PFN_WDFDRIVERREGISTERTRACEINFO
title: PFN_WDFDRIVERREGISTERTRACEINFO function
author: windows-driver-content
description: The WdfDriverRegisterTraceInfo method is reserved for internal use only.
old-location: wdf\wdfdriverregistertraceinfo.htm
old-project: wdf
ms.assetid: f2d332cd-d744-444c-b616-d8400ad30d43
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: PFN_WDFDRIVERREGISTERTRACEINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WdfDriverRegisterTraceInfo
req.alt-loc: Wdfdriver.h
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Not applicable
req.typenames: WDF_DPC_CONFIG, *PWDF_DPC_CONFIG
req.product: Windows 10 or later.
---

# PFN_WDFDRIVERREGISTERTRACEINFO function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDriverRegisterTraceInfo</b> method is reserved for internal use only.



## -syntax

````
NTSTATUS WdfDriverRegisterTraceInfo(
  _In_ PDRIVER_OBJECT         DriverObject,
  _In_ PFN_WDF_TRACE_CALLBACK EvtTraceCallback,
  _In_ PVOID                  ControlBlock
);
````


## -parameters

### -param DriverObject [in]


### -param EvtTraceCallback [in]


### -param ControlBlock [in]


## -remarks
