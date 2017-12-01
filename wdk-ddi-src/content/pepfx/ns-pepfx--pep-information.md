---
UID: NS.pepfx._PEP_INFORMATION
title: PEP_INFORMATION
author: windows-driver-content
description: The PEP_INFORMATION structure specifies the interface that the platform extension plug-in (PEP) uses to receive notifications from the Windows power management framework (PoFx).
old-location: kernel\pep_information.htm
old-project: kernel
ms.assetid: 60221D44-79C0-4043-A4AF-1200C2F087F6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_INFORMATION, PEP_INFORMATION, *PPEP_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_INFORMATION
req.alt-loc: pepfx.h
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

# PEP_INFORMATION structure



## -description
<p>The <b>PEP_INFORMATION</b> structure specifies the interface that the platform extension plug-in (PEP) uses to receive notifications from the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx).</p>


## -syntax

````
typedef struct _PEP_INFORMATION {
  USHORT                 Version;
  USHORT                 Size;
  PPEPCALLBACKNOTIFYDPM  AcceptDeviceNotification;
  PPEPCALLBACKNOTIFYPPM  AcceptProcessorNotification;
  PPEPCALLBACKNOTIFYACPI AcceptAcpiNotification;
} PEP_INFORMATION, *PPEP_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The current version number for this structure. Set this member to PEP_INFORMATION_VERSION.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure. Set this member to <b>sizeof</b>(<b>PEP_INFORMATION</b>).</p>
</dd>

### -field <b>AcceptDeviceNotification</b>

<dd>
<p>A pointer to an <a href="kernel.acceptdevicenotification">AcceptDeviceNotification</a> callback routine. This member is required to point to a valid callback routine.</p>
</dd>

### -field <b>AcceptProcessorNotification</b>

<dd>
<p>A pointer to an <a href="kernel.acceptprocessornotification">AcceptProcessorNotification</a> callback routine. This member is optional and can be NULL if the PEP is not prepared to handle PPM notifications from PoFx.</p>
</dd>

### -field <b>AcceptAcpiNotification</b>

<dd>
<p>A pointer to an <a href="kernel.acceptacpinotification">AcceptAcpiNotification</a> callback routine. This member is optional and can be NULL if the PEP is not prepared to handle ACPI notifications from PoFx.</p>
</dd>
</dl>

## -remarks
<p>This structure contains pointers to several callback routines that are implemented by the PEP. PoFx calls these routines to send notifications to the PEP.</p>

<p>The <i>PepInformation</i> parameter to the <a href="..\pepfx\nf-pepfx-pofxregisterplugin.md">PoFxRegisterPlugin</a> and <a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a> routines is a pointer to a <b>PEP_INFORMATION</b> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.acceptacpinotification">AcceptAcpiNotification</a>
</dt>
<dt>
<a href="kernel.acceptdevicenotification">AcceptDeviceNotification</a>
</dt>
<dt>
<a href="kernel.acceptprocessornotification">AcceptProcessorNotification</a>
</dt>
<dt>
<a href="..\pepfx\nf-pepfx-pofxregisterplugin.md">PoFxRegisterPlugin</a>
</dt>
<dt>
<a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_INFORMATION structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
