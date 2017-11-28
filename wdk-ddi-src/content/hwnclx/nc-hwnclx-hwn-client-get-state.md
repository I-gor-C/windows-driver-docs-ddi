---
UID: NC.hwnclx.HWN_CLIENT_GET_STATE
title: HWN_CLIENT_GET_STATE
author: windows-driver-content
description: Implemented by the client driver to get hardware notification component state. It is invoked when a user requests status information.
old-location: gpiobtn\hwn_client_get_state.htm
old-project: gpiobtn
ms.assetid: c472b4bf-4c7f-4c30-ad03-2017d26d52b4
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: HPMI_QUERY_CAPABILITIES, HPMI_QUERY_CAPABILITIES, *PHPMI_QUERY_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hwnclx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PHWN_CLIENT_GET_STATE
req.alt-loc: Hwnclx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# HWN_CLIENT_GET_STATE callback



## -description
<p>
Implemented by the client driver to get hardware notification component state. It is invoked when a user requests status information.</p>


## -prototype

````
HWN_CLIENT_GET_STATE HwnClientGetState;

NTSTATUS HwnClientGetState(
  _In_  PVOID  Context,
  _Out_ PVOID  OutputBuffer,
  _In_  ULONG  OutputBufferLength,
  _In_  PVOID  InputBuffer,
  _In_  ULONG  InputBufferLength,
  _Out_ PULONG BytesRead
)
{ ... }

typedef HWN_CLIENT_GET_STATE *PHWN_CLIENT_GET_STATE;
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to the client driver's context information. This memory space is available for use by the client driver. It is allocated as part of the framework object context space by <b>WdfDeviceCreate</b>. For more information, see <a href="gpiobtn.hwn_client_registration_packet">HWN_CLIENT_REGISTRATION_PACKET</a> and  <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/framework-object-context-space">Framework Object Context Space</a>.</p>
</dd>

### -param <i>OutputBuffer</i> [out]

<dd>
<p>Buffer of <i>OutputBufferLength</i> bytes for writing hardware notification status. If the function succeeds, the buffer will contain a <a href="gpiobtn.hwn_header">HWN_HEADER</a> structure including one or more <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structures.</p>
<div class="alert"><b>Note</b>  <p class="note"><b>OutputBufferLength</b> must be large enough to contain all of the requested settings. For more information, see Remarks.</p>
</div>
<div> </div>
</dd>

### -param <i>OutputBufferLength</i> [in]

<dd>
<p>The size of <i>OutputBuffer</i> in bytes.</p>
</dd>

### -param <i>InputBuffer</i> [in]

<dd>
<p>Buffer of <i>InputBufferLength</i> bytes containing a <a href="gpiobtn.hwn_header">HWN_HEADER</a> holding one or more <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structures where the IDs for the requested hardware notification components are stored in the <b>HwNId</b> field. This buffer can be NULL.</p>
</dd>

### -param <i>InputBufferLength</i> [in]

<dd>
<p>The size of <i>InputBuffer</i> in bytes.</p>
</dd>

### -param <i>BytesRead</i> [out]

<dd>
<p>Pointer to a variable that indicates the number of bytes read by the function.</p>
</dd>
</dl>

## -returns
<p>
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.</p>

## -remarks
<p>Register your implementation of this callback function by setting the appropriate member of <a href="gpiobtn.hwn_client_registration_packet">HWN_CLIENT_REGISTRATION_PACKET</a> and then calling <a href="..\hwnclx\nf-hwnclx-hwnregisterclient.md">HwNRegisterClient</a>.</p>

<p>If <i>InputBuffer</i> is NULL, the output buffer will be used to store a <a href="gpiobtn.hwn_header">HWN_HEADER</a> structure that contains all of the settings for the hardware notifications implemented by the driver. </p>

<p>The Settings for a hardware notification component are stored in a <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structure. The <b>HwNSettingsInfo</b> field of the <a href="gpiobtn.hwn_header">HWN_HEADER</a> structure contains an array of <b>HWN_SETTINGS</b> structures.</p>

<p>If <i>InputBuffer</i> is not null and is correctly formatted, it will contain a <a href="gpiobtn.hwn_header">HWN_HEADER</a> with one or more <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structures. The IDs for the requested hardware notification components are stored in the <b>HwNId</b> field of the <b>HWN_SETTINGS</b> structure. The remaining settings should be valid settings or zero.</p>

<p>If <i>OutputBuffer</i> is not large enough to contain all of the settings requested, this function should not write anything to <i>OutputBuffer</i>. Additionally, it should set <i>BytesRead</i> to 0 and return an error.</p>

<p>Register your implementation of this callback function by setting the appropriate member of <a href="gpiobtn.hwn_client_registration_packet">HWN_CLIENT_REGISTRATION_PACKET</a> and then calling <a href="..\hwnclx\nf-hwnclx-hwnregisterclient.md">HwNRegisterClient</a>.</p>

<p>If <i>InputBuffer</i> is NULL, the output buffer will be used to store a <a href="gpiobtn.hwn_header">HWN_HEADER</a> structure that contains all of the settings for the hardware notifications implemented by the driver. </p>

<p>The Settings for a hardware notification component are stored in a <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structure. The <b>HwNSettingsInfo</b> field of the <a href="gpiobtn.hwn_header">HWN_HEADER</a> structure contains an array of <b>HWN_SETTINGS</b> structures.</p>

<p>If <i>InputBuffer</i> is not null and is correctly formatted, it will contain a <a href="gpiobtn.hwn_header">HWN_HEADER</a> with one or more <a href="gpiobtn.hwn_settings">HWN_SETTINGS</a> structures. The IDs for the requested hardware notification components are stored in the <b>HwNId</b> field of the <b>HWN_SETTINGS</b> structure. The remaining settings should be valid settings or zero.</p>

<p>If <i>OutputBuffer</i> is not large enough to contain all of the settings requested, this function should not write anything to <i>OutputBuffer</i>. Additionally, it should set <i>BytesRead</i> to 0 and return an error.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hwnclx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><a href="https://msdn.microsoft.com/en-us/library/windows/hardware/dn789335">Hardware notifications support</a></dt>
<dt>
<a href="gpiobtn.hardware_notifications_reference">Hardware notifications reference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [gpiobtn\gpiobtn]:%20HWN_CLIENT_GET_STATE callback function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
