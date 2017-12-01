---
UID: NS.pepfx._PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES
title: PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES
author: windows-driver-content
description: The PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure contains a list of translated power-control resources for the platform extension plug-in (PEP) to use.
old-location: kernel\pep_acpi_translated_device_control_resources.htm
old-project: kernel
ms.assetid: 1274EF11-6A0D-4464-992D-4E27C981971F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES,
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
req.alt-api: PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES
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

# PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure



## -description
<p>The <b>PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES</b> structure contains a list of translated power-control resources for the platform extension plug-in (PEP) to use.</p>


## -syntax

````
struct PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES {
  PEPHANDLE        DeviceHandle;
  ULONG            RequestFlags;
  NTSTATUS         Status;
  SIZE_T           ResourceBufferSize;
  CM_RESOURCE_LIST TranslatedResources;
};
````


## -struct-fields
<dl>

### -field <b>DeviceHandle</b>

<dd>
<p>[in] A PEPHANDLE value that identifies the device's registration for ACPI services. The platform extension plug-in (PEP) supplied this handle in response to a previous <a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a> notification.</p>
</dd>

### -field <b>RequestFlags</b>

<dd>
<p>[in] A set of input flags. No flags are currently defined for this member, which is always set to PEP_ACPI_TDCR_FLAG_NONE (0x0).</p>
</dd>

### -field <b>Status</b>

<dd>
<p>[out] An NTSTATUS value that indicates the status of the resource translation. The PEP sets this member to STATUS_SUCCESS to indicate that the PEP successfully received the translated resources. Otherwise, the PEP sets this member to an appropriate error status code.</p>
</dd>

### -field <b>ResourceBufferSize</b>

<dd>
<p>[in] The size in bytes of the input buffer that contains both this structure and the resource-list data that follows this structure.</p>
</dd>

### -field <b>TranslatedResources</b>

<dd>
<p>[in] A <a href="..\wdm\ns-wdm--cm-resource-list.md">CM_RESOURCE_LIST</a> structure that serves as the header for the resource list. The remainder of the resource list immediately follows this header.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by the <a href="kernel.pep_notify_acpi_translated_device_control_resources">PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES</a> notification to provide the PEP with a list of translated power control resources. The <b>RequestFlags</b>, <b>ResourceBufferSize</b>, and <b>TranslatedResources</b> members of the structure contain input values that the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx) supplies when this notification is sent. The <b>Status</b> member contains an output value that the PEP writes to the structure in response to the notification.</p>

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
<a href="..\wdm\ns-wdm--cm-resource-list.md">CM_RESOURCE_LIST</a>
</dt>
<dt>
<a href="kernel.pep_notify_acpi_register_device">PEP_NOTIFY_ACPI_REGISTER_DEVICE</a>
</dt>
<dt>
<a href="kernel.pep_notify_acpi_translated_device_control_resources">PEP_NOTIFY_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_ACPI_TRANSLATED_DEVICE_CONTROL_RESOURCES structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
