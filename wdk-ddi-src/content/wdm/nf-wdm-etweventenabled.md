---
UID: NF:wdm.EtwEventEnabled
title: EtwEventEnabled function
author: windows-driver-content
description: The EtwEventEnabled function verifies whether an event is enabled.
old-location: devtest\etweventenabled.htm
old-project: devtest
ms.assetid: 19aa5905-f611-46e2-8d70-a6cc4649c911
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: EtwEventEnabled, EtwEventEnabled function [Driver Development Tools], devtest.etweventenabled, etw_km_4a6453a7-cff8-4941-83fd-8184772ef161.xml, wdm/EtwEventEnabled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	EtwEventEnabled
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# EtwEventEnabled function
The <b>EtwEventEnabled</b> function verifies whether an event is enabled.

## Syntax

````
BOOLEAN EtwEventEnabled(
  _In_ REGHANDLE          RegHandle,
  _In_ PCEVENT_DESCRIPTOR EventDescriptor
);
````

## Parameters

`RegHandle`

A pointer to the event provider registration handle, which is returned by the 
      <b>EtwRegister</b> function if the event provider registration is successful.

`EventDescriptor`

A pointer to a constant EVENT_DESCRIPTOR.


## Return Value

The <b>EtwEventEnabled</b> function returns <b>TRUE</b> if the 
      event is enabled and <b>FALSE</b> if the event is not enabled.

## Remarks

If logging an event requires additional computing, the <b>EtwEventEnabled</b> 
     function can be used to determine whether the event is going to be logged, which will minimize the overhead when 
     logging is disabled.

If the event descriptor is not available, use the 
     <a href="..\wdm\nf-wdm-etwproviderenabled.md">EtwProviderEnabled</a> function instead.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | Any level |

## See Also

<a href="..\wdm\nf-wdm-etwproviderenabled.md">EtwProviderEnabled</a>