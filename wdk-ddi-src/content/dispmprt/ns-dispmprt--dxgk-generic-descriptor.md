---
UID: NS.dispmprt._DXGK_GENERIC_DESCRIPTOR
title: DXGK_GENERIC_DESCRIPTOR
author: windows-driver-content
description: The DXGK_GENERIC_DESCRIPTOR structure contains descriptive information about a child device of the display adapter.
old-location: display\dxgk_generic_descriptor.htm
old-project: display
ms.assetid: 181df1a6-044d-406d-bc6d-1b35b3d744fc
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_GENERIC_DESCRIPTOR, DXGK_GENERIC_DESCRIPTOR, *PDXGK_GENERIC_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GENERIC_DESCRIPTOR
req.alt-loc: dispmprt.h
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

# DXGK_GENERIC_DESCRIPTOR structure



## -description
<p>The DXGK_GENERIC_DESCRIPTOR structure contains descriptive information about a child device of the display adapter.</p>


## -syntax

````
typedef struct _DXGK_GENERIC_DESCRIPTOR {
  WCHAR HardwareId[DXGK_MAX_REG_SZ_LEN];
  WCHAR InstanceId[DXGK_MAX_REG_SZ_LEN];
  WCHAR CompatibleId[DXGK_MAX_REG_SZ_LEN];
  WCHAR DeviceText[DXGK_MAX_REG_SZ_LEN];
} DXGK_GENERIC_DESCRIPTOR, *PDXGK_GENERIC_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>HardwareId</b>

<dd>
<p>A single wide-character string, terminated by two wide NULL characters, that holds the hardware ID of the child device.</p>
</dd>

### -field <b>InstanceId</b>

<dd>
<p>A single wide-character string, terminated by two wide NULL characters, that holds the instance ID of the child device.</p>
</dd>

### -field <b>CompatibleId</b>

<dd>
<p>A sequence of wide-character strings, each of which is terminated by a single wide NULL character. The last string in the sequence is terminated by two wide NULL characters.</p>
</dd>

### -field <b>DeviceText</b>

<dd>
<p>A single wide-character string, terminated by two wide NULL characters, that holds the device text of the child device.</p>
</dd>
</dl>

## -remarks
<p>The display adapter has two types of child devices: <b>TypeVideoOutput</b> and <b>TypeOther</b>. For child devices of type <b>TypeOther</b>, the display port driver passes a DXGK_GENERIC_DESCRIPTOR structure to the display miniport driver's <a href="display.dxgkddiquerydevicedescriptor">DxgkDdiQueryDeviceDescriptor</a> function. <i>DxgkDdiQueryDeviceDescriptor</i> must fill in the members of the structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561050">DXGK_DEVICE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_GENERIC_DESCRIPTOR structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
