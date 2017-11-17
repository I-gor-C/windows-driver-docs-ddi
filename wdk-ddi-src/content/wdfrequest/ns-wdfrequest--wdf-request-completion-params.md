---
UID: NS.wdfrequest._WDF_REQUEST_COMPLETION_PARAMS
title: WDF_REQUEST_COMPLETION_PARAMS
author: windows-driver-content
description: The WDF_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request.
old-location: wdf\wdf_request_completion_params.htm
ms.assetid: e3993202-c49d-4de9-8881-9e3786575e17
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_COMPLETION_PARAMS
req.alt-loc: wdfrequest.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_REQUEST_COMPLETION_PARAMS, WDF_REQUEST_COMPLETION_PARAMS, *PWDF_REQUEST_COMPLETION_PARAMS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_COMPLETION_PARAMS structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure contains parameters that are associated with the completion of an I/O request.</p>


## -syntax

````
typedef struct _WDF_REQUEST_COMPLETION_PARAMS {
  ULONG            Size;
  WDF_REQUEST_TYPE Type;
  IO_STATUS_BLOCK  IoStatus;
  union {
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } Write;
    struct {
      WDFMEMORY Buffer;
      size_t    Length;
      size_t    Offset;
    } Read;
    struct {
      ULONG  IoControlCode;
      struct {
        WDFMEMORY Buffer;
        size_t    Offset;
      } Input;
      struct {
        WDFMEMORY Buffer;
        size_t    Offset;
        size_t    Length;
      } Output;
    } Ioctl;
    struct {
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument1;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument2;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument3;
      union {
        PVOID     Ptr;
        ULONG_PTR Value;
      } Argument4;
    } Others;
    struct {
      PWDF_USB_REQUEST_COMPLETION_PARAMS Completion;
    } Usb;
  } Parameters;
} WDF_REQUEST_COMPLETION_PARAMS, *PWDF_REQUEST_COMPLETION_PARAMS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a> value that identifies the request type.</p>
</dd>

### -field <b>IoStatus</b>

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure for the request.</p>
</dd>

### -field <b>Parameters</b>

<dd>
<p>Request-specific values for the request.</p>
<dl>

### -field <b>Write</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>A handle to a framework memory object. This object identifies the buffer that the driver specified when it formatted the request and sent it to an I/O target.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length, in bytes, of the transfer.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Beginning address within the buffer for the data transfer.</p>
</dd>
</dl>
</dd>

### -field <b>Read</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>A handle to a framework memory object. This object identifies the buffer that the driver specified when it formatted the request and sent it to an I/O target.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length, in bytes, of the transfer.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Beginning address within the buffer for the data transfer.</p>
</dd>
</dl>
</dd>

### -field <b>Ioctl</b>

<dd>
<dl>

### -field <b>Input</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>A handle to a framework memory object. This object identifies the input buffer that the driver specified when it formatted the request and sent it to an I/O target.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Beginning address within the buffer for the data transfer.</p>
</dd>
</dl>
</dd>

### -field <b>Output</b>

<dd>
<dl>

### -field <b>Buffer</b>

<dd>
<p>A handle to a framework memory object. This object identifies the output buffers that the driver specified when it formatted the request and sent it to an I/O target.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>Beginning address within the buffer for the data transfer.</p>
</dd>

### -field <b>Length</b>

<dd>
<p>Length, in bytes, of the transfer.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>Others</b>

<dd>
<dl>

### -field <b>Argument1</b>

<dd>
<p>Use of this member is defined by the driver stack.  See Remarks.</p>
</dd>

### -field <b>Argument2</b>

<dd>
<p>Use of this member is defined by the driver stack.</p>
</dd>

### -field <b>Argument3</b>

<dd>
<p>Use of this member is defined by the driver stack.</p>
</dd>

### -field <b>Argument4</b>

<dd>
<p>Use of this member is defined by the driver stack.</p>
</dd>
</dl>
</dd>

### -field <b>Usb</b>

<dd>
<p>For USB devices, this member contains a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553049">WDF_USB_REQUEST_COMPLETION_PARAMS</a> structure.

</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a> method and a driver's <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function.</p>

<p> In both cases, the completion parameters structure contains valid information only if the driver has formatted the request by calling one of the <b>WdfIoTargetFormat</b><i>Xxx</i> methods. For example, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548612">WdfIoTargetFormatRequestForRead</a>.</p>

<p>Before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a> to retrieve the I/O completion information for a request, the driver must first call <a href="https://msdn.microsoft.com/library/windows/hardware/ff552456">WDF_REQUEST_COMPLETION_PARAMS_INIT</a> to initialize the <b>WDF_REQUEST_COMPLETION_PARAMS</b> structure.</p>

<p>The <b>Parameters.Others.Argument</b>  members are custom arguments that a driver typically passes down the stack (and can arrive back after the request is completed).  They are used for non-standard, driver stack dependent data. For example, a USB driver specifies a pointer to a URB in  <b>Parameters.Others.Argument1</b> when it sends a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537271">IOCTL_INTERNAL_USB_SUBMIT_URB</a> request to the USB stack.  Similarly, a Bluetooth driver specifies a pointer to a  BRB (Bluetooth Request Block) in <b>Parameters.Others.Argument1</b> when it receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536751">IOCTL_INTERNAL_BTH_SUBMIT_BRB</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfrequest.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549961">WdfRequestGetCompletionParams</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552456">WDF_REQUEST_COMPLETION_PARAMS_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552503">WDF_REQUEST_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_COMPLETION_PARAMS structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
