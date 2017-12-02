---
UID: NS.wdm._CM_KEYBOARD_DEVICE_DATA
title: CM_KEYBOARD_DEVICE_DATA
author: windows-driver-content
description: The CM_KEYBOARD_DEVICE_DATA structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a keyboard peripheral if the system can collect this information during the boot process.
old-location: kernel\cm_keyboard_device_data.htm
old-project: kernel
ms.assetid: 928cc1b6-4569-4ca1-9410-d864b5556b86
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: CM_KEYBOARD_DEVICE_DATA, CM_KEYBOARD_DEVICE_DATA, *PCM_KEYBOARD_DEVICE_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CM_KEYBOARD_DEVICE_DATA
req.alt-loc: wdm.h
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

# CM_KEYBOARD_DEVICE_DATA structure



## -description
<p>The <b>CM_KEYBOARD_DEVICE_DATA</b> structure defines a device-type-specific data record that is stored in the \\Registry\Machine\Hardware\Description tree for a keyboard peripheral if the system can collect this information during the boot process.</p>


## -syntax

````
typedef struct _CM_KEYBOARD_DEVICE_DATA {
  USHORT Version;
  USHORT Revision;
  UCHAR  Type;
  UCHAR  Subtype;
  USHORT KeyboardFlags;
} CM_KEYBOARD_DEVICE_DATA, *PCM_KEYBOARD_DEVICE_DATA;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The version number of this structure.</p>
</dd>

### -field Revision

<dd>
<p>The revision of this structure.</p>
</dd>

### -field Type

<dd>
<p>The type of the keyboard.</p>
</dd>

### -field Subtype

<dd>
<p>The subtype of the keyboard.</p>
</dd>

### -field KeyboardFlags

<dd>
<p>Defined by x86 BIOS INT 16h, function 02 as:</p>
<table>
<tr>
<th>Bit</th>
<th>Defined As</th>
</tr>
<tr>
<td>
<p>7</p>
</td>
<td>
<p>Insert on.</p>
</td>
</tr>
<tr>
<td>
<p>6</p>
</td>
<td>
<p>Caps Lock on.</p>
</td>
</tr>
<tr>
<td>
<p>5</p>
</td>
<td>
<p>Num Lock on.</p>
</td>
</tr>
<tr>
<td>
<p>4</p>
</td>
<td>
<p>Scroll Lock on.</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>Alt Key is down.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>Ctrl Key is down.</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>Left shift key is down.</p>
</td>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>Right shift key is down.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549453">IoQueryDeviceDescription</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549616">IoReportResourceUsage</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_KEYBOARD_DEVICE_DATA structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
