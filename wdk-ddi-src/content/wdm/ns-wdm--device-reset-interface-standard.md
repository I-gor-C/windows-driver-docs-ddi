---
UID: NS.wdm._DEVICE_RESET_INTERFACE_STANDARD
title: DEVICE_RESET_INTERFACE_STANDARD
author: windows-driver-content
description: The DEVICE_RESET_INTERFACE_STANDARD structure enables function drivers to reset and recover malfunctioning devices. This structure describes the GUID_DEVICE_RESET_INTERFACE_STANDARD interface.
old-location: kernel\device_reset_interface_standard.htm
old-project: kernel
ms.assetid: DD8A7E50-664B-49B8-905B-A5BE02A48DCE
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: DEVICE_RESET_INTERFACE_STANDARD, DEVICE_RESET_INTERFACE_STANDARD, *PDEVICE_RESET_INTERFACE_STANDARD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_RESET_INTERFACE_STANDARD
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_RESET_INTERFACE_STANDARD structure



## -description
<p>The <b>DEVICE_RESET_INTERFACE_STANDARD</b> structure enables function drivers to reset and recover malfunctioning devices. This structure describes the <a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a> interface.</p>


## -syntax

````
typedef struct _DEVICE_RESET_INTERFACE_STANDARD {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PDEVICE_RESET_HANDLER  DeviceReset;
  PVOID                  Reserved;
} DEVICE_RESET_INTERFACE_STANDARD, *PDEVICE_RESET_INTERFACE_STANDARD;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The driver-defined interface version.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to interface-specific context information</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a> routine that increments the interface's reference count.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff547829">InterfaceDereference</a> routine that decrements the interface's reference count.</p>
</dd>

### -field <b>DeviceReset</b>

<dd>
<p>A pointer to the interface's <a href="https://msdn.microsoft.com/library/windows/hardware/dn939354">DeviceReset</a> routine. This routine can be used by function drivers to attempt to reset and recover a malfunctioning device.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved for future use.</p>
</dd>
</dl>

## -remarks
<p>The <b>DEVICE_RESET_INTERFACE_STANDARD</b> structure is an extension of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure. A driver obtains a pointer to the <b>DEVICE_RESET_INTERFACE_STANDARD</b> structure by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> IRP to its bus driver with <b>InterfaceType</b> set to GUID_DEVICE_RESET_INTERFACE_STANDARD.</p>

<p>For more information about the purpose of this interface, see <a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>.</p>

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
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn928420">GUID_DEVICE_RESET_INTERFACE_STANDARD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn939354">DeviceReset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547829">InterfaceDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_RESET_INTERFACE_STANDARD structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
