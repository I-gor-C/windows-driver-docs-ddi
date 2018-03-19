---
UID: NF:wdm.CmCallbackReleaseKeyObjectIDEx
title: CmCallbackReleaseKeyObjectIDEx function
author: windows-driver-content
description: The CmCallbackReleaseKeyObjectIDEx routine frees an object name string obtained from the CmCallbackGetKeyObjectIDEx routine.
old-location: kernel\cmcallbackreleasekeyobjectidex.htm
old-project: kernel
ms.assetid: 3361DAEF-AC2A-401B-80E8-0220F191587C
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: CmCallbackReleaseKeyObjectIDEx, CmCallbackReleaseKeyObjectIDEx routine [Kernel-Mode Driver Architecture], kernel.cmcallbackreleasekeyobjectidex, wdm/CmCallbackReleaseKeyObjectIDEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
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
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	CmCallbackReleaseKeyObjectIDEx
product: Windows
targetos: Windows
req.typenames: WORK_QUEUE_TYPE
req.product: Windows 10 or later.
---


# CmCallbackReleaseKeyObjectIDEx function
The <b>CmCallbackReleaseKeyObjectIDEx</b> routine frees an object name string obtained from the <a href="..\wdm\nf-wdm-cmcallbackgetkeyobjectidex.md">CmCallbackGetKeyObjectIDEx</a> routine.

## Syntax

````
VOID CmCallbackReleaseKeyObjectIDEx(
   PCUNICODE_STRING ObjectName
);
````

## Parameters

`ObjectName`

A pointer to a <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> structure that contains the object name string. The driver previously obtained this pointer by calling <a href="..\wdm\nf-wdm-cmcallbackgetkeyobjectidex.md">CmCallbackGetKeyObjectIDEx</a>.


## Return Value

None.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a>



<a href="..\wdm\nf-wdm-cmcallbackgetkeyobjectidex.md">CmCallbackGetKeyObjectIDEx</a>