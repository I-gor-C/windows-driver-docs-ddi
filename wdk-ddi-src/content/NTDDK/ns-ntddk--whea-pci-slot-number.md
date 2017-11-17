---
UID: NS.ntddk._WHEA_PCI_SLOT_NUMBER
title: WHEA_PCI_SLOT_NUMBER
author: windows-driver-content
description: The WHEA_PCI_SLOT_NUMBER structure describes a logical PCI slot.
old-location: whea\whea_pci_slot_number.htm
ms.assetid: 4e2938a2-6301-4d2a-a467-eca1f5bbb260
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_PCI_SLOT_NUMBER
req.alt-loc: ntddk.h
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
ms.keywords: WHEA_PCI_SLOT_NUMBER, WHEA_PCI_SLOT_NUMBER, *PWHEA_PCI_SLOT_NUMBER
req.iface: 
---

# WHEA_PCI_SLOT_NUMBER structure



## -description
<p>The WHEA_PCI_SLOT_NUMBER structure describes a logical PCI slot.</p>


## -syntax

````
typedef struct _WHEA_PCI_SLOT_NUMBER {
  union {
    struct {
      ULONG DeviceNumber  :5;
      ULONG FunctionNumber  :3;
      ULONG Reserved  :24;
    } bits;
    ULONG  AsULONG;
  } u;
} WHEA_PCI_SLOT_NUMBER, *PWHEA_PCI_SLOT_NUMBER;
````


## -struct-fields
<dl>

### -field <b>u</b>

<dd>
<p>A union that contains the following members:</p>
<dl>

### -field <b>bits</b>

<dd>
<p>A structure that describes the logical PCI slot.</p>
<dl>

### -field <b>DeviceNumber</b>

<dd>
<p>The device number that is assigned to the logical PCI slot. </p>
</dd>

### -field <b>FunctionNumber</b>

<dd>
<p>The specific function on the device that is located in the logical PCI slot. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. </p>
</dd>
</dl>
</dd>

### -field <b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the WHEA_PCI_SLOT_NUMBER structure.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>A WHEA_PCI_SLOT_NUMBER structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560446">WHEA_AER_BRIDGE_DESCRIPTOR</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff560447">WHEA_AER_ENDPOINT_DESCRIPTOR</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff560450">WHEA_AER_ROOTPORT_DESCRIPTOR</a> structures.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560446">WHEA_AER_BRIDGE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560447">WHEA_AER_ENDPOINT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560450">WHEA_AER_ROOTPORT_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_PCI_SLOT_NUMBER structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
