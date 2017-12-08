---
UID: NE.wdfrequest._WDF_REQUEST_TYPE
title: WDF_REQUEST_TYPE
author: windows-driver-content
description: The WDF_REQUEST_TYPE enumeration type identifies types of requests that a framework request object might contain.
old-location: wdf\wdf_request_type.htm
old-project: wdf
ms.assetid: 91c036a0-7fce-4c7d-a217-eb1c487a15d0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfRegistryWdmGetHandle
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

### -field WdfRequestTypeCreate

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request. The framework delivers this type of request to a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-file-create.md">EvtDeviceFileCreate</a> callback function.</p>
</dd>

### -field WdfRequestTypeCreateNamedPipe

<dd>
<p>The request object represents an <b>IRP_MJ_CREATE_NAMED_PIPE</b> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeClose

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550720">IRP_MJ_CLOSE</a> request. The framework delivers this type of request to a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-close.md">EvtFileClose</a> callback function.</p>
</dd>

### -field WdfRequestTypeRead

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field WdfRequestTypeWrite

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field WdfRequestTypeQueryInformation

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549283">IRP_MJ_QUERY_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeSetInformation

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549366">IRP_MJ_SET_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeQueryEA

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_query_ea">IRP_MJ_QUERY_EA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeSetEA

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_set_ea">IRP_MJ_SET_EA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeFlushBuffers

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeQueryVolumeInformation

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_query_volume_information">IRP_MJ_QUERY_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeSetVolumeInformation

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_set_volume_information">IRP_MJ_SET_VOLUME_INFORMATION</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeDirectoryControl

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_directory_control">IRP_MJ_DIRECTORY_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeFileSystemControl

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550751">IRP_MJ_FILE_SYSTEM_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeDeviceControl

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field WdfRequestTypeDeviceControlInternal

<dd>
<p>The request object represents an  <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a> request. The framework delivers this type of request to a driver's <a href="wdf.request_handlers">request handler</a>.</p>
</dd>

### -field WdfRequestTypeShutdown

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="wdf.evtdeviceshutdownnotification">EvtDeviceShutdownNotification</a> callback function, if it exists.</p>
</dd>

### -field WdfRequestTypeLockControl

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_lock_control">IRP_MJ_LOCK_CONTROL</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeCleanup

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548608">IRP_MJ_CLEANUP</a> request. The framework delivers this type of request to a driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-cleanup.md">EvtFileCleanup</a> callback function.</p>
</dd>

### -field WdfRequestTypeCreateMailSlot

<dd>
<p>The request object represents an <b>IRP_MJ_CREATE_MAILSLOT</b> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeQuerySecurity

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_query_security">IRP_MJ_QUERY_SECURITY</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeSetSecurity

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_set_security">IRP_MJ_SET_SECURITY</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypePower

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550784">IRP_MJ_POWER</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="wdf_device_object_reference.htm#device_callbacks">general</a>, <a href="wdf_device_object_reference.htm#fdo_callbacks">FDO</a>, and <a href="wdf_device_object_reference.htm#pdo_callbacks">PDO</a> callback functions for Plug and Play (PnP) and power management, if the callback functions exist.</p>
</dd>

### -field WdfRequestTypeSystemControl

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550813">IRP_MJ_SYSTEM_CONTROL</a> request. The framework handles this type of request for the driver, if the driver supports <a href="wdf.supporting_wmi_in_kmdf_drivers">Windows Management Instrumentation (WMI)</a>.</p>
</dd>

### -field WdfRequestTypeDeviceChange

<dd>
<p>The request object represents an <b>IRP_MJ_DEVICE_CHANGE</b> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeQueryQuota

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_query_quota">IRP_MJ_QUERY_QUOTA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypeSetQuota

<dd>
<p>The request object represents an <a href="ifsk.irp_mj_set_quota">IRP_MJ_SET_QUOTA</a> request. The framework does not handle this type of request.</p>
</dd>

### -field WdfRequestTypePnp

<dd>
<p>The request object represents an <a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a> request. The framework handles this type of request for the driver, but the framework also calls the driver's <a href="wdf_device_object_reference.htm#device_callbacks">general</a>, <a href="wdf_device_object_reference.htm#fdo_callbacks">FDO</a>, and <a href="wdf_device_object_reference.htm#pdo_callbacks">PDO</a> callback functions for PnP and power management, if the callback functions exist.</p>
</dd>

### -field WdfRequestTypeOther

<dd>
<p>A driver receives this request type in its <a href="..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md">CompletionRoutine</a> event callback function when requests formatted with <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers.md">WdfIoTargetFormatRequestForInternalIoctlOthers</a> are completed.</p>
</dd>

### -field WdfRequestTypeUsb

<dd>
<p>The target device is a USB device. (This value is used only in <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structures.)</p>
</dd>

### -field WdfRequestTypeNoFormat

<dd>
<p>The request object's type has not been specified.</p>
</dd>

### -field WdfRequestTypeMax

<dd>
<p>The maximum value that has been assigned to a valid IRP major function code.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_REQUEST_TYPE</b> enumeration type is used in the <a href="..\wdfrequest\ns-wdfrequest--wdf-request-parameters.md">WDF_REQUEST_PARAMETERS</a> and <a href="..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md">WDF_REQUEST_COMPLETION_PARAMS</a> structures.</p>

<p>For information about how a framework-based driver can handle request types that the framework does not support, see <a href="wdf.handling_an_irp_that_the_framework_does_not_support">Handling an IRP that the Framework Does Not Support</a>.</p>

<p>For the UMDF version of this enumeration, see <a href="..\wudfddi_types\ne-wudfddi-types--wdf-request-type.md">WDF_REQUEST_TYPE (UMDF)</a>.</p>

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
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-file-create.md">EvtDeviceFileCreate</a>
</dt>
<dt>
<a href="wdf.evtdeviceshutdownnotification">EvtDeviceShutdownNotification</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-cleanup.md">EvtFileCleanup</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-close.md">EvtFileClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
