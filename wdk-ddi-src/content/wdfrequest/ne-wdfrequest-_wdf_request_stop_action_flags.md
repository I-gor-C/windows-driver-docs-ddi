---
UID: NE:wdfrequest._WDF_REQUEST_STOP_ACTION_FLAGS
title: "_WDF_REQUEST_STOP_ACTION_FLAGS"
author: windows-driver-content
description: The WDF_REQUEST_STOP_ACTION_FLAGS enumeration type defines flags that the framework passes to a driver's EvtIoStop callback function.
old-location: wdf\wdf_request_stop_action_flags.htm
old-project: wdf
ms.assetid: 01f95aee-60aa-4d6f-88a9-c0fa6ea6a09a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFRequestObjectRef_e291c6a5-1e65-4505-9090-19e6ea66e7b3.xml, WDF_REQUEST_STOP_ACTION_FLAGS, WDF_REQUEST_STOP_ACTION_FLAGS enumeration, WdfRequestStopActionInvalid, WdfRequestStopActionPurge, WdfRequestStopActionSuspend, WdfRequestStopRequestCancelable, _WDF_REQUEST_STOP_ACTION_FLAGS, kmdf.wdf_request_stop_action_flags, wdf.wdf_request_stop_action_flags, wdfrequest/WDF_REQUEST_STOP_ACTION_FLAGS, wdfrequest/WdfRequestStopActionInvalid, wdfrequest/WdfRequestStopActionPurge, wdfrequest/WdfRequestStopActionSuspend, wdfrequest/WdfRequestStopRequestCancelable
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfrequest.h
api_name:
-	WDF_REQUEST_STOP_ACTION_FLAGS
product:
- Windows
targetos: Windows
req.typenames: WDF_REQUEST_STOP_ACTION_FLAGS
req.product: Windows 10 or later.
---

# _WDF_REQUEST_STOP_ACTION_FLAGS Enumeration
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_REQUEST_STOP_ACTION_FLAGS</b> enumeration type defines flags that the framework passes to a driver's <a href="https://msdn.microsoft.com/71a789f1-4f10-44c3-8bd0-a0ea74ec28ab">EvtIoStop</a> callback function.

## Syntax
```
typedef enum _WDF_REQUEST_STOP_ACTION_FLAGS {
  WdfRequestStopActionInvalid      ,
  WdfRequestStopActionSuspend      ,
  WdfRequestStopActionPurge        ,
  WdfRequestStopRequestCancelable
} WDF_REQUEST_STOP_ACTION_FLAGS;
```

## Constants

<table>
            
                <tr>
                    <td>WdfRequestStopActionInvalid</td>
                    <td>Reserved for internal use only.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestStopActionSuspend</td>
                    <td>The framework is stopping the I/O queue because the device is leaving its working (D0) state.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestStopActionPurge</td>
                    <td>The framework is stopping the I/O queue because the device is being removed.</td>
                </tr>
            
                <tr>
                    <td>WdfRequestStopRequestCancelable</td>
                    <td>The I/O request is cancelable.</td>
                </tr>
</table>

## Remarks

When the framework calls a driver's <a href="https://msdn.microsoft.com/71a789f1-4f10-44c3-8bd0-a0ea74ec28ab">EvtIoStop</a> callback function, it sets either the <b>WdfRequestStopActionSuspend</b> or <b>WdfRequestStopActionPurge</b> flag. If the request is cancelable, the framework also sets the <b>WdfRequestStopRequestCancelable</b> flag.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfrequest.h (include Wdf.h) |

## See Also

<a href="https://msdn.microsoft.com/71a789f1-4f10-44c3-8bd0-a0ea74ec28ab">EvtIoStop</a>