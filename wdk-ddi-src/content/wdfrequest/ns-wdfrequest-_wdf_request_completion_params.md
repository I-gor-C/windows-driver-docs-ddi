---
UID: NS:wdfrequest._WDF_REQUEST_COMPLETION_PARAMS
title: "_WDF_REQUEST_COMPLETION_PARAMS"
author: windows-driver-content
description: The WDF_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request.
old-location: wdf\wdf_request_completion_params.htm
old-project: wdf
ms.assetid: e3993202-c49d-4de9-8881-9e3786575e17
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: "*PWDF_REQUEST_COMPLETION_PARAMS, DFRequestObjectRef_e8277b90-7e1e-4d00-9f6b-012b189c153f.xml, PWDF_REQUEST_COMPLETION_PARAMS, PWDF_REQUEST_COMPLETION_PARAMS structure pointer, WDF_REQUEST_COMPLETION_PARAMS, WDF_REQUEST_COMPLETION_PARAMS structure, _WDF_REQUEST_COMPLETION_PARAMS, kmdf.wdf_request_completion_params, wdf.wdf_request_completion_params, wdfrequest/PWDF_REQUEST_COMPLETION_PARAMS, wdfrequest/WDF_REQUEST_COMPLETION_PARAMS"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	WDF_REQUEST_COMPLETION_PARAMS
product:
- Windows
targetos: Windows
req.typenames: WDF_REQUEST_COMPLETION_PARAMS, *PWDF_REQUEST_COMPLETION_PARAMS
req.product: Windows 10 or later.
---

# _WDF_REQUEST_COMPLETION_PARAMS structure
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure contains parameters that are associated with the completion of an I/O request.

## Syntax
```
typedef struct _WDF_REQUEST_COMPLETION_PARAMS {
  ULONG            Size;
  WDF_REQUEST_TYPE Type;
  IO_STATUS_BLOCK  IoStatus;
  union {
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } Write;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } Read;
    struct {
      ULONG  IoControlCode;
      struct {
        WDFMEMORY Buffer;
        size_t    Offset;
      } Input;
      struct {
        WDFMEMORY Buffer;
        size_t    Length;
        size_t    Offset;
      } Output;
    } Ioctl;
    struct {
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument1;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument2;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument3;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument4;
    } Others;
    struct {
      PWDF_USB_REQUEST_COMPLETION_PARAMS Completion;
    } Usb;
  } Parameters;
} WDF_REQUEST_COMPLETION_PARAMS, *PWDF_REQUEST_COMPLETION_PARAMS;
```

## Members


`Size`

The size, in bytes, of this structure.

`Type`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a> value that identifies the request type.

`IoStatus`

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure for the request.

`Parameters`

Request-specific values for the request.

## Remarks
The <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a> method and a driver's <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function.

 In both cases, the completion parameters structure contains valid information only if the driver has formatted the request by calling one of the <b>WdfIoTargetFormat</b><i>Xxx</i> methods. For example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548612">WdfIoTargetFormatRequestForRead</a>.

Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a> to retrieve the I/O completion information for a request, the driver must first call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552456">WDF_REQUEST_COMPLETION_PARAMS_INIT</a> to initialize the <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure.

The <b>Parameters.Others.Argument</b>  members are custom arguments that a driver typically passes down the stack (and can arrive back after the request is completed).  They are used for non-standard, driver stack dependent data. For example, a USB driver specifies a pointer to a URB in  <b>Parameters.Others.Argument1</b> when it sends a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537271">IOCTL_INTERNAL_USB_SUBMIT_URB</a> request to the USB stack.  Similarly, a Bluetooth driver specifies a pointer to a  BRB (Bluetooth Request Block) in <b>Parameters.Others.Argument1</b> when it receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536751">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfrequest.h (include Wdf.h) |

## See Also

<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552456">WDF_REQUEST_COMPLETION_PARAMS_INIT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a>