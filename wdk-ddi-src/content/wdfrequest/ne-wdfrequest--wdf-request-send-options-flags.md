---
UID: NE.wdfrequest._WDF_REQUEST_SEND_OPTIONS_FLAGS
title: WDF_REQUEST_SEND_OPTIONS_FLAGS
author: windows-driver-content
description: The WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_SEND_OPTIONS structure.
old-location: wdf\wdf_request_send_options_flags.htm
ms.assetid: 68be1034-62f0-4444-b4c9-097277a7561f
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
req.alt-api: WDF_REQUEST_SEND_OPTIONS_FLAGS
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

# WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_REQUEST_SEND_OPTIONS_FLAGS</b> enumeration type defines flags that are used in a driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure.</p>


## -syntax

````
typedef enum _WDF_REQUEST_SEND_OPTIONS_FLAGS { 
  WDF_REQUEST_SEND_OPTION_TIMEOUT                       = 0x0000001,
  WDF_REQUEST_SEND_OPTION_SYNCHRONOUS                   = 0x0000002,
  WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE           = 0x0000004,
  WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET               = 0x0000008,
  WDF_REQUEST_SEND_OPTION_IMPERSONATE_CLIENT            = 0x00010000,
  WDF_REQUEST_SEND_OPTION_IMPERSONATION_IGNORE_FAILURE  = 0x00020000
} WDF_REQUEST_SEND_OPTIONS_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDF_REQUEST_SEND_OPTION_TIMEOUT"></a><a id="wdf_request_send_option_timeout"></a><b>WDF_REQUEST_SEND_OPTION_TIMEOUT</b>

<dd>
<p>If the driver sets this flag, the <b>Timeout</b> member of the WDF_REQUEST_SEND_OPTIONS structure is valid.</p>
</dd>

### -field <a id="WDF_REQUEST_SEND_OPTION_SYNCHRONOUS"></a><a id="wdf_request_send_option_synchronous"></a><b>WDF_REQUEST_SEND_OPTION_SYNCHRONOUS</b>

<dd>
<p>If the driver sets this flag, the framework handles the associated I/O request synchronously. (The driver does not have to set this flag if it is calling an object method whose name ends with "Synchronously", such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff548669">WdfIoTargetSendReadSynchronously</a>.)</p>
</dd>

### -field <a id="WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE"></a><a id="wdf_request_send_option_ignore_target_state"></a><b>WDF_REQUEST_SEND_OPTION_IGNORE_TARGET_STATE</b>

<dd>
<p>If the driver sets this flag, the framework sends the I/O request to the I/O target, regardless of the I/O target's state. If not set, the framework queues the request if the target is stopped. Setting this flag allows a driver to send a request, such as a request to reset a USB pipe, to a device after the driver has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>.</p>
</dd>

### -field <a id="WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET"></a><a id="wdf_request_send_option_send_and_forget"></a><b>WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET</b>

<dd>
<p>If the driver sets this flag, the driver is sending the request asynchronously and does not need to be notified when the request is completed or canceled. The framework sends the I/O request to the I/O target, regardless of the I/O target's state. The driver does not set a <a href="https://msdn.microsoft.com/7d3eb4d6-9fc7-4924-9b95-f5824713049b">CompletionRoutine</a> callback function or call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549945">WdfRequestComplete</a> for the request. If the driver sets this flag, it cannot set any other flags. For more information about this flag, see the following Remarks section.</p>
</dd>

### -field <a id="WDF_REQUEST_SEND_OPTION_IMPERSONATE_CLIENT"></a><a id="wdf_request_send_option_impersonate_client"></a><b>WDF_REQUEST_SEND_OPTION_IMPERSONATE_CLIENT</b>

<dd>
<p>This flag applies to UMDF only. If set, and if the I/O request type is <b>WdfRequestTypeCreate</b>, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> method attempts to pass the client's impersonation level to the driver's I/O target. The <b>WdfRequestSend</b> method returns an error code if the impersonation attempt fails, unless the driver also sets the <b>WDF_REQUEST_SEND_OPTION_IMPERSONATION_IGNORE_FAILURE</b> flag.</p>
</dd>

### -field <a id="WDF_REQUEST_SEND_OPTION_IMPERSONATION_IGNORE_FAILURE"></a><a id="wdf_request_send_option_impersonation_ignore_failure"></a><b>WDF_REQUEST_SEND_OPTION_IMPERSONATION_IGNORE_FAILURE</b>

<dd>
<p>This flag applies to UMDF only. If set, the framework still sends the request even if impersonation fails.  You can use this value only with <b>WDF_REQUEST_SEND_OPTION_IMPERSONATE_CLIENT</b>.</p>
</dd>
</dl>

## -remarks
<p>A driver that sets the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag typically does not format the I/O request before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> to send the request to an I/O target. In fact, a driver that sets this flag must not call any of the <b>WdfIoTargetFormatRequestFor</b><i>Xxx</i> methods before it calls <b>WdfRequestSend</b>. The driver can use only the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549955">WdfRequestFormatRequestUsingCurrentType</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550036">WdfRequestWdmFormatUsingStackLocation</a> method to format the request.</p>

<p>Your driver <i>cannot</i> set the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag in the following situations:</p>

<p>The driver created the request object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target and the driver specified the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenByName</a> flag when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target, and the driver specified both the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenUseExistingDevice</a> flag and a <a href="https://msdn.microsoft.com/9539868c-127b-4781-9a73-b56fbfda3233">TargetFileObject</a> pointer when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The request type is <a href="https://msdn.microsoft.com/91c036a0-7fce-4c7d-a217-eb1c487a15d0">WdfRequestTypeCreate</a> and the driver has not set the <a href="https://msdn.microsoft.com/e0887061-eafe-4dba-bb7a-58bf949e2d08">WdfFileObjectNotRequired</a> flag. (For more information about this situation, see <a href="wdf.framework_file_objects">Framework File Objects</a>.)</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561462">WDF_REQUEST_SEND_OPTIONS_FLAGS (UMDF)</a>.</p>

<p>A driver that sets the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag typically does not format the I/O request before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> to send the request to an I/O target. In fact, a driver that sets this flag must not call any of the <b>WdfIoTargetFormatRequestFor</b><i>Xxx</i> methods before it calls <b>WdfRequestSend</b>. The driver can use only the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549955">WdfRequestFormatRequestUsingCurrentType</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550036">WdfRequestWdmFormatUsingStackLocation</a> method to format the request.</p>

<p>Your driver <i>cannot</i> set the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag in the following situations:</p>

<p>The driver created the request object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target and the driver specified the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenByName</a> flag when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target, and the driver specified both the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenUseExistingDevice</a> flag and a <a href="https://msdn.microsoft.com/9539868c-127b-4781-9a73-b56fbfda3233">TargetFileObject</a> pointer when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The request type is <a href="https://msdn.microsoft.com/91c036a0-7fce-4c7d-a217-eb1c487a15d0">WdfRequestTypeCreate</a> and the driver has not set the <a href="https://msdn.microsoft.com/e0887061-eafe-4dba-bb7a-58bf949e2d08">WdfFileObjectNotRequired</a> flag. (For more information about this situation, see <a href="wdf.framework_file_objects">Framework File Objects</a>.)</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561462">WDF_REQUEST_SEND_OPTIONS_FLAGS (UMDF)</a>.</p>

<p>A driver that sets the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag typically does not format the I/O request before it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550027">WdfRequestSend</a> to send the request to an I/O target. In fact, a driver that sets this flag must not call any of the <b>WdfIoTargetFormatRequestFor</b><i>Xxx</i> methods before it calls <b>WdfRequestSend</b>. The driver can use only the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549955">WdfRequestFormatRequestUsingCurrentType</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550036">WdfRequestWdmFormatUsingStackLocation</a> method to format the request.</p>

<p>Your driver <i>cannot</i> set the WDF_REQUEST_SEND_OPTION_SEND_AND_FORGET flag in the following situations:</p>

<p>The driver created the request object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549951">WdfRequestCreate</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target and the driver specified the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenByName</a> flag when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The driver is sending the I/O request to a remote I/O target, and the driver specified both the <a href="https://msdn.microsoft.com/27aa5d78-03ce-4fc9-b1c8-d02a760e2787">WdfIoTargetOpenUseExistingDevice</a> flag and a <a href="https://msdn.microsoft.com/9539868c-127b-4781-9a73-b56fbfda3233">TargetFileObject</a> pointer when it called <a href="https://msdn.microsoft.com/library/windows/hardware/ff548634">WdfIoTargetOpen</a>.</p>

<p>The request type is <a href="https://msdn.microsoft.com/91c036a0-7fce-4c7d-a217-eb1c487a15d0">WdfRequestTypeCreate</a> and the driver has not set the <a href="https://msdn.microsoft.com/e0887061-eafe-4dba-bb7a-58bf949e2d08">WdfFileObjectNotRequired</a> flag. (For more information about this situation, see <a href="wdf.framework_file_objects">Framework File Objects</a>.)</p>

<p>For the UMDF version of this enumeration, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561462">WDF_REQUEST_SEND_OPTIONS_FLAGS (UMDF)</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548680">WdfIoTargetStop</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
