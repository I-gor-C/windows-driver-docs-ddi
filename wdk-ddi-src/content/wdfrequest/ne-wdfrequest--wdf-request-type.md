---
UID: NE.wdfrequest._WDF_REQUEST_TYPE
title: WDF_REQUEST_TYPE
author: windows-driver-content
description: The WDF_REQUEST_TYPE enumeration type identifies types of requests that a framework request object might contain.
old-location: wdf\wdf_request_type.htm
ms.assetid: 91c036a0-7fce-4c7d-a217-eb1c487a15d0
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfrequest.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_REQUEST_TYPE
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
req.irql: 
ms.keywords: WdfRegistryWdmGetHandle
req.iface: 
req.product: Windows 10 or later.
---

# WDF_REQUEST_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_TYPE</b> enumeration type identifies types of requests that a framework request object might contain.</p>


## -syntax

````
typedef enum _WDF_REQUEST_TYPE { 
  WdfRequestTypeCreate                  = 0x0,
  WdfRequestTypeCreateNamedPipe         = 0x1,
  WdfRequestTypeClose                   = 0x2,
  WdfRequestTypeRead                    = 0x3,
  WdfRequestTypeWrite                   = 0x4,
  WdfRequestTypeQueryInformation        = 0x5,
  WdfRequestTypeSetInformation          = 0x6,
  WdfRequestTypeQueryEA                 = 0x7,
  WdfRequestTypeSetEA                   = 0x8,
  WdfRequestTypeFlushBuffers            = 0x9,
  WdfRequestTypeQueryVolumeInformation  = 0xa,
  WdfRequestTypeSetVolumeInformation    = 0xb,
  WdfRequestTypeDirectoryControl        = 0xc,
  WdfRequestTypeFileSystemControl       = 0xd,
  WdfRequestTypeDeviceControl           = 0xe,
  WdfRequestTypeDeviceControlInternal   = 0xf,
  WdfRequestTypeShutdown                = 0x10,
  WdfRequestTypeLockControl             = 0x11,
  WdfRequestTypeCleanup                 = 0x12,
  WdfRequestTypeCreateMailSlot          = 0x13,
  WdfRequestTypeQuerySecurity           = 0x14,
  WdfRequestTypeSetSecurity             = 0x15,
  WdfRequestTypePower                   = 0x16,
  WdfRequestTypeSystemControl           = 0x17,
  WdfRequestTypeDeviceChange            = 0x18,
  WdfRequestTypeQueryQuota              = 0x19,
  WdfRequestTypeSetQuota                = 0x1A,
  WdfRequestTypePnp                     = 0x1B,
  WdfRequestTypeOther                   = 0x1C,
  WdfRequestTypeUsb                     = 0x40,
  WdfRequestTypeNoFormat                = 0xFF,
  WdfRequestTypeMax                     = 0x100
} WDF_REQUEST_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfRequestTypeCreate"></a><a id="wdfrequesttypecreate"></a><a id="WDFREQUESTTYPECREATE"></a><b>WdfRequestTypeCreate</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a> callback function.</p>
</dd>

### -field <a id="WdfRequestTypeCreateNamedPipe"></a><a id="wdfrequesttypecreatenamedpipe"></a><a id="WDFREQUESTTYPECREATENAMEDPIPE"></a><b>WdfRequestTypeCreateNamedPipe</b>

<dd>
<p>The request object represents an <b>IRP_MJ_CREATE_NAMED_PIPE</b> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeClose"></a><a id="wdfrequesttypeclose"></a><a id="WDFREQUESTTYPECLOSE"></a><b>WdfRequestTypeClose</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a> callback function.</p>
</dd>

### -field <a id="WdfRequestTypeRead"></a><a id="wdfrequesttyperead"></a><a id="WDFREQUESTTYPEREAD"></a><b>WdfRequestTypeRead</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field <a id="WdfRequestTypeWrite"></a><a id="wdfrequesttypewrite"></a><a id="WDFREQUESTTYPEWRITE"></a><b>WdfRequestTypeWrite</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field <a id="WdfRequestTypeQueryInformation"></a><a id="wdfrequesttypequeryinformation"></a><a id="WDFREQUESTTYPEQUERYINFORMATION"></a><b>WdfRequestTypeQueryInformation</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeSetInformation"></a><a id="wdfrequesttypesetinformation"></a><a id="WDFREQUESTTYPESETINFORMATION"></a><b>WdfRequestTypeSetInformation</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeQueryEA"></a><a id="wdfrequesttypequeryea"></a><a id="WDFREQUESTTYPEQUERYEA"></a><b>WdfRequestTypeQueryEA</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549279">IRP_MJ_QUERY_EA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeSetEA"></a><a id="wdfrequesttypesetea"></a><a id="WDFREQUESTTYPESETEA"></a><b>WdfRequestTypeSetEA</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549346">IRP_MJ_SET_EA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeFlushBuffers"></a><a id="wdfrequesttypeflushbuffers"></a><a id="WDFREQUESTTYPEFLUSHBUFFERS"></a><b>WdfRequestTypeFlushBuffers</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeQueryVolumeInformation"></a><a id="wdfrequesttypequeryvolumeinformation"></a><a id="WDFREQUESTTYPEQUERYVOLUMEINFORMATION"></a><b>WdfRequestTypeQueryVolumeInformation</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549318">IRP_MJ_QUERY_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeSetVolumeInformation"></a><a id="wdfrequesttypesetvolumeinformation"></a><a id="WDFREQUESTTYPESETVOLUMEINFORMATION"></a><b>WdfRequestTypeSetVolumeInformation</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549415">IRP_MJ_SET_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeDirectoryControl"></a><a id="wdfrequesttypedirectorycontrol"></a><a id="WDFREQUESTTYPEDIRECTORYCONTROL"></a><b>WdfRequestTypeDirectoryControl</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548658">IRP_MJ_DIRECTORY_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeFileSystemControl"></a><a id="wdfrequesttypefilesystemcontrol"></a><a id="WDFREQUESTTYPEFILESYSTEMCONTROL"></a><b>WdfRequestTypeFileSystemControl</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550751">IRP_MJ_FILE_SYSTEM_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeDeviceControl"></a><a id="wdfrequesttypedevicecontrol"></a><a id="WDFREQUESTTYPEDEVICECONTROL"></a><b>WdfRequestTypeDeviceControl</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field <a id="WdfRequestTypeDeviceControlInternal"></a><a id="wdfrequesttypedevicecontrolinternal"></a><a id="WDFREQUESTTYPEDEVICECONTROLINTERNAL"></a><b>WdfRequestTypeDeviceControlInternal</b>

<dd>
<p>The request object represents an  <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field <a id="WdfRequestTypeShutdown"></a><a id="wdfrequesttypeshutdown"></a><a id="WDFREQUESTTYPESHUTDOWN"></a><b>WdfRequestTypeShutdown</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="https://msdn.microsoft.com/365e669b-b4a1-432a-ab0c-9292a910256e">EvtDeviceShutdownNotification</a> callback function, if it exists.</p>
</dd>

### -field <a id="WdfRequestTypeLockControl"></a><a id="wdfrequesttypelockcontrol"></a><a id="WDFREQUESTTYPELOCKCONTROL"></a><b>WdfRequestTypeLockControl</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549251">IRP_MJ_LOCK_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeCleanup"></a><a id="wdfrequesttypecleanup"></a><a id="WDFREQUESTTYPECLEANUP"></a><b>WdfRequestTypeCleanup</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a> request. The framework delivers this type of request to a driver's <a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a> callback function.</p>
</dd>

### -field <a id="WdfRequestTypeCreateMailSlot"></a><a id="wdfrequesttypecreatemailslot"></a><a id="WDFREQUESTTYPECREATEMAILSLOT"></a><b>WdfRequestTypeCreateMailSlot</b>

<dd>
<p>The request object represents an <b>IRP_MJ_CREATE_MAILSLOT</b> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeQuerySecurity"></a><a id="wdfrequesttypequerysecurity"></a><a id="WDFREQUESTTYPEQUERYSECURITY"></a><b>WdfRequestTypeQuerySecurity</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549298">IRP_MJ_QUERY_SECURITY</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeSetSecurity"></a><a id="wdfrequesttypesetsecurity"></a><a id="WDFREQUESTTYPESETSECURITY"></a><b>WdfRequestTypeSetSecurity</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549407">IRP_MJ_SET_SECURITY</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypePower"></a><a id="wdfrequesttypepower"></a><a id="WDFREQUESTTYPEPOWER"></a><b>WdfRequestTypePower</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="wdf_device_object_reference.htm#device_callbacks">general</a>, <a href="wdf_device_object_reference.htm#fdo_callbacks">FDO</a>, and <a href="wdf_device_object_reference.htm#pdo_callbacks">PDO</a> callback functions for Plug and Play (PnP) and power management, if the callback functions exist.</p>
</dd>

### -field <a id="WdfRequestTypeSystemControl"></a><a id="wdfrequesttypesystemcontrol"></a><a id="WDFREQUESTTYPESYSTEMCONTROL"></a><b>WdfRequestTypeSystemControl</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550813">IRP_MJ_SYSTEM_CONTROL</a> request. The framework handles this type of request for the driver, if the driver supports <a href="wdf.supporting_wmi_in_kmdf_drivers">Windows Management Instrumentation (WMI)</a>.</p>
</dd>

### -field <a id="WdfRequestTypeDeviceChange"></a><a id="wdfrequesttypedevicechange"></a><a id="WDFREQUESTTYPEDEVICECHANGE"></a><b>WdfRequestTypeDeviceChange</b>

<dd>
<p>The request object represents an <b>IRP_MJ_DEVICE_CHANGE</b> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeQueryQuota"></a><a id="wdfrequesttypequeryquota"></a><a id="WDFREQUESTTYPEQUERYQUOTA"></a><b>WdfRequestTypeQueryQuota</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549293">IRP_MJ_QUERY_QUOTA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypeSetQuota"></a><a id="wdfrequesttypesetquota"></a><a id="WDFREQUESTTYPESETQUOTA"></a><b>WdfRequestTypeSetQuota</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549401">IRP_MJ_SET_QUOTA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field <a id="WdfRequestTypePnp"></a><a id="wdfrequesttypepnp"></a><a id="WDFREQUESTTYPEPNP"></a><b>WdfRequestTypePnp</b>

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="wdf_device_object_reference.htm#device_callbacks">general</a>, <a href="wdf_device_object_reference.htm#fdo_callbacks">FDO</a>, and <a href="wdf_device_object_reference.htm#pdo_callbacks">PDO</a> callback functions for PnP and power management, if the callback functions exist.</p>
</dd>

### -field <a id="WdfRequestTypeOther"></a><a id="wdfrequesttypeother"></a><a id="WDFREQUESTTYPEOTHER"></a><b>WdfRequestTypeOther</b>

<dd>
<p>A driver receives this request type in its <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> event callback function when requests formatted with <a href="https://msdn.microsoft.com/library/windows/hardware/ff548599">WdfIoTargetFormatRequestForInternalIoctlOthers</a> are completed.</p>
</dd>

### -field <a id="WdfRequestTypeUsb"></a><a id="wdfrequesttypeusb"></a><a id="WDFREQUESTTYPEUSB"></a><b>WdfRequestTypeUsb</b>

<dd>
<p>The target device is a USB device. (This value is used only in <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.)</p>
</dd>

### -field <a id="WdfRequestTypeNoFormat"></a><a id="wdfrequesttypenoformat"></a><a id="WDFREQUESTTYPENOFORMAT"></a><b>WdfRequestTypeNoFormat</b>

<dd>
<p>The request object's type has not been specified.</p>
</dd>

### -field <a id="WdfRequestTypeMax"></a><a id="wdfrequesttypemax"></a><a id="WDFREQUESTTYPEMAX"></a><b>WdfRequestTypeMax</b>

<dd>
<p>The maximum value that has been assigned to a valid IRP major function code.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_TYPE</b> enumeration type is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552472">WDF_REQUEST_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.</p>

<p>For information about how a framework-based driver can handle request types that the framework does not support, see <a href="wdf.handling_an_irp_that_the_framework_does_not_support">Handling an IRP that the Framework Does Not Support</a>.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561467">WDF_REQUEST_TYPE (UMDF)</a>.</p>

<p>The <b>WDF_REQUEST_TYPE</b> enumeration type is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552472">WDF_REQUEST_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.</p>

<p>For information about how a framework-based driver can handle request types that the framework does not support, see <a href="wdf.handling_an_irp_that_the_framework_does_not_support">Handling an IRP that the Framework Does Not Support</a>.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561467">WDF_REQUEST_TYPE (UMDF)</a>.</p>

<p>The <b>WDF_REQUEST_TYPE</b> enumeration type is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552472">WDF_REQUEST_PARAMETERS</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552454">WDF_REQUEST_COMPLETION_PARAMS</a> structures.</p>

<p>For information about how a framework-based driver can handle request types that the framework does not support, see <a href="wdf.handling_an_irp_that_the_framework_does_not_support">Handling an IRP that the Framework Does Not Support</a>.</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561467">WDF_REQUEST_TYPE (UMDF)</a>.</p>

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
<a href="https://msdn.microsoft.com/ee44c0bf-1fca-442d-8871-df6079e89ced">EvtDeviceFileCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/365e669b-b4a1-432a-ab0c-9292a910256e">EvtDeviceShutdownNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8ce3d316-3976-4af5-a0ae-af4e93f380a1">EvtFileCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8ddcb9cb-d184-4ec8-a321-599394a8512e">EvtFileClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_TYPE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
