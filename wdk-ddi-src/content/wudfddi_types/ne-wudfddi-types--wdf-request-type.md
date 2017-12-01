---
UID: NE.wudfddi_types._WDF_REQUEST_TYPE
title: WDF_REQUEST_TYPE
author: windows-driver-content
description: The WDF_REQUEST_TYPE enumeration identifies the types of I/O requests that a UMDF request object can represent.
old-location: wdf\wdf_request_type__umdf_.htm
old-project: wdf
ms.assetid: a883f22e-0d6f-4755-882b-ad5a60a09271
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WRITE_REGISTER_USHORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wudfddi_types.h
req.include-header: Wudfddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDF_REQUEST_TYPE
req.alt-loc: Wudfddi_types.h
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_TYPE enumeration



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>
      The <b>WDF_REQUEST_TYPE</b> enumeration identifies the types of I/O requests that a UMDF request object can represent.</p>


## -syntax

````
typedef enum _WDF_REQUEST_TYPE { 
  WdfRequestUndefined          = 0,
  WdfRequestCreate             = 1,
  WdfRequestCleanup            = 2,
  WdfRequestRead               = 3,
  WdfRequestWrite              = 4,
  WdfRequestDeviceIoControl    = 5,
  WdfRequestClose              = 6,
  WdfRequestUsb                = 7,
  WdfRequestOther              = 8,
  WdfRequestInternalIoctl      = 9,
  WdfRequestTypeNoFormat       = 10,
  WdfRequestFlushBuffers       = 11,
  WdfRequestQueryInformation   = 12,
  WdfRequestSetInformation     = 13,
  WdfRequestMaximum
} WDF_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfRequestUndefined"></a><a id="wdfrequestundefined"></a><a id="WDFREQUESTUNDEFINED"></a><b>WdfRequestUndefined</b>

<dd>
<p>The type of the request object is undefined.</p>
</dd>

### -field <a id="WdfRequestCreate"></a><a id="wdfrequestcreate"></a><a id="WDFREQUESTCREATE"></a><b>WdfRequestCreate</b>

<dd>
<p>The request object represents a file creation request. The driver receives this type of request object when an application opens a device by calling the Microsoft Win32 <b>CreateFile</b> function. The framework delivers this type of request, along with a newly created file object (<a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a>), to the driver's <a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a> callback function. The new file object represents the HANDLE-typed file handle that the Win32 <b>CreateFile</b> returns. </p>
</dd>

### -field <a id="WdfRequestCleanup"></a><a id="wdfrequestcleanup"></a><a id="WDFREQUESTCLEANUP"></a><b>WdfRequestCleanup</b>

<dd>
<p> The request object represents a file cleanup request. The driver receives this type of request object after an application's call to the Win32 <b>CloseHandle</b> function closes the last handle to a file object, but possibly before all of the file's outstanding I/O requests have been completed or canceled. The framework delivers this type of request to the driver's <a href="wdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a> callback function. (Also see <b>WdfRequestClose</b>.)</p>
</dd>

### -field <a id="WdfRequestRead"></a><a id="wdfrequestread"></a><a id="WDFREQUESTREAD"></a><b>WdfRequestRead</b>

<dd>
<p>The request object represents a read request. This driver receives this type of I/O request when an application calls the Win32 <b>ReadFile</b> or <b>ReadFileEx</b> function. The framework delivers this type of request to the driver's <a href="wdf.iqueuecallbackread_onread">IQueueCallbackRead::OnRead</a> callback function.</p>
</dd>

### -field <a id="WdfRequestWrite"></a><a id="wdfrequestwrite"></a><a id="WDFREQUESTWRITE"></a><b>WdfRequestWrite</b>

<dd>
<p>The request object represents a write request. This driver receives this type of I/O request when an application calls the Win32 <b>WriteFile</b> or <b>WriteFileEx</b> function. The framework delivers this type of request to  the driver's <a href="wdf.iqueuecallbackwrite_onwrite">IQueueCallbackWrite::OnWrite</a> callback function.</p>
</dd>

### -field <a id="WdfRequestDeviceIoControl"></a><a id="wdfrequestdeviceiocontrol"></a><a id="WDFREQUESTDEVICEIOCONTROL"></a><b>WdfRequestDeviceIoControl</b>

<dd>
<p>The request object represents a device I/O control request. This driver receives this type of I/O request when an application calls the Win32 <b>DeviceIoControl</b> function. The framework delivers this type of request to  the driver's <a href="wdf.iqueuecallbackdeviceiocontrol_ondeviceiocontrol">IQueueCallbackDeviceIoControl::OnDeviceIoControl</a> callback function.</p>
</dd>

### -field <a id="WdfRequestClose"></a><a id="wdfrequestclose"></a><a id="WDFREQUESTCLOSE"></a><b>WdfRequestClose</b>

<dd>
<p>The request object represents a file close request.  The driver receives this type of request object after an application's call to the Win32 <b>CloseHandle</b> function closes the last handle to a file object, and after all of the file's outstanding I/O requests have been completed or canceled.  The framework delivers this type of request to the driver's <a href="wdf.ifilecallbackclose_onclosefile">IFileCallbackClose::OnCloseFile</a> callback function. (Also see <b>WdfRequestCleanup</b>.)</p>
</dd>

### -field <a id="WdfRequestUsb"></a><a id="wdfrequestusb"></a><a id="WDFREQUESTUSB"></a><b>WdfRequestUsb</b>

<dd>
<p>The request object was sent to a USB port. The <a href="wdf.iwdfrequestcompletionparams_getcompletedrequesttype">IWDFRequestCompletionParams::GetCompletedRequestType</a> method can return this value. </p>
</dd>

### -field <a id="WdfRequestOther"></a><a id="wdfrequestother"></a><a id="WDFREQUESTOTHER"></a><b>WdfRequestOther</b>

<dd>
<p>This value is reserved for internal use only.</p>
</dd>

### -field <a id="WdfRequestInternalIoctl"></a><a id="wdfrequestinternalioctl"></a><a id="WDFREQUESTINTERNALIOCTL"></a><b>WdfRequestInternalIoctl</b>

<dd>
<p>This value is reserved for internal use only.</p>
</dd>

### -field <a id="WdfRequestTypeNoFormat"></a><a id="wdfrequesttypenoformat"></a><a id="WDFREQUESTTYPENOFORMAT"></a><b>WdfRequestTypeNoFormat</b>

<dd>
<p>The request object's type has not been specified.</p>
</dd>

### -field <a id="WdfRequestFlushBuffers_"></a><a id="wdfrequestflushbuffers_"></a><a id="WDFREQUESTFLUSHBUFFERS_"></a><b>WdfRequestFlushBuffers </b>

<dd>
<p>The request object represents a request to flush cached buffers. The framework delivers this type of request to the driver's <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">IQueueCallbackDefaultIoHandler::OnDefaultIoHandler</a> callback function. </p>
</dd>

### -field <a id="WdfRequestQueryInformation_"></a><a id="wdfrequestqueryinformation_"></a><a id="WDFREQUESTQUERYINFORMATION_"></a><b>WdfRequestQueryInformation </b>

<dd>
<p>The request object represents a request to obtain information about a file. The framework delivers this type of request to the driver's <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">IQueueCallbackDefaultIoHandler::OnDefaultIoHandler</a> callback function. </p>
</dd>

### -field <a id="WdfRequestSetInformation"></a><a id="wdfrequestsetinformation"></a><a id="WDFREQUESTSETINFORMATION"></a><b>WdfRequestSetInformation</b>

<dd>
<p>The request object represents a request to set information about a file. The framework delivers this type of request to the driver's <a href="wdf.iqueuecallbackdefaultiohandler_ondefaultiohandler">IQueueCallbackDefaultIoHandler::OnDefaultIoHandler</a> callback function. </p>
</dd>

### -field <a id="WdfRequestMaximum"></a><a id="wdfrequestmaximum"></a><a id="WDFREQUESTMAXIMUM"></a><b>WdfRequestMaximum</b>

<dd>
<p>The maximum value for the enumeration is exceeded.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_TYPE</b> enumeration is used as an input parameter of <a href="wdf.iwdfdevice_configurerequestdispatching">IWDFDevice::ConfigureRequestDispatching</a> and <a href="wdf.iwdfioqueue_configurerequestdispatching">IWDFIoQueue::ConfigureRequestDispatching</a>. It is also used for the return value of <a href="wdf.iwdfiorequest_gettype">IWDFIoRequest::GetType</a> and <a href="wdf.iwdfrequestcompletionparams_getcompletedrequesttype">IWDFRequestCompletionParams::GetCompletedRequestType</a>.</p>

<p>For the KMDF version of this enumeration, see <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-type.md">WDF_REQUEST_TYPE</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi_types.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.ifilecallbackcleanup_oncleanupfile">IFileCallbackCleanup::OnCleanupFile</a>
</dt>
<dt>
<a href="wdf.ifilecallbackclose_onclosefile">IFileCallbackClose::OnCloseFile</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackcreate_oncreatefile">IQueueCallbackCreate::OnCreateFile</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackdeviceiocontrol_ondeviceiocontrol">IQueueCallbackDeviceIoControl::OnDeviceIoControl</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackread_onread">IQueueCallbackRead::OnRead</a>
</dt>
<dt>
<a href="wdf.iqueuecallbackwrite_onwrite">IQueueCallbackWrite::OnWrite</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_TYPE enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
