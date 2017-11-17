---
UID: NS.ntddk._WHEA_AER_BRIDGE_DESCRIPTOR
title: WHEA_AER_BRIDGE_DESCRIPTOR
author: windows-driver-content
description: The WHEA_AER_BRIDGE_DESCRIPTOR structure describes a PCI Express (PCIe) bridge error source.
old-location: whea\whea_aer_bridge_descriptor.htm
ms.assetid: 33cc9d34-cffb-410d-9948-37c8a409e0a5
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
req.alt-api: WHEA_AER_BRIDGE_DESCRIPTOR
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
ms.keywords: WHEA_AER_BRIDGE_DESCRIPTOR, WHEA_AER_BRIDGE_DESCRIPTOR, *PWHEA_AER_BRIDGE_DESCRIPTOR
req.iface: 
---

# WHEA_AER_BRIDGE_DESCRIPTOR structure



## -description
<p>The WHEA_AER_BRIDGE_DESCRIPTOR structure describes a PCI Express (PCIe) bridge error source.</p>


## -syntax

````
typedef struct _WHEA_AER_BRIDGE_DESCRIPTOR {
  USHORT                      Type;
  BOOLEAN                     Enabled;
  UCHAR                       Reserved;
  ULONG                       BusNumber;
  WHEA_PCI_SLOT_NUMBER        Slot;
  USHORT                      DeviceControl;
  AER_BRIDGE_DESCRIPTOR_FLAGS Flags;
  ULONG                       UncorrectableErrorMask;
  ULONG                       UncorrectableErrorSeverity;
  ULONG                       CorrectableErrorMask;
  ULONG                       AdvancedCapsAndControl;
  ULONG                       SecondaryUncorrectableErrorMask;
  ULONG                       SecondaryUncorrectableErrorSev;
  ULONG                       SecondaryCapsAndControl;
} WHEA_AER_BRIDGE_DESCRIPTOR, *PWHEA_AER_BRIDGE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of error source descriptor. This member is always set to WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERBRIDGE.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>A Boolean value that indicates if the error source is enabled.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>BusNumber</b>

<dd>
<p>The bridge's primary bus number.</p>
</dd>

### -field <b>Slot</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560595">WHEA_PCI_SLOT_NUMBER</a> structure that describes the logical PCI slot where the bridge is located in the system.</p>
</dd>

### -field <b>DeviceControl</b>

<dd>
<p>The contents of the bridge's Device Control register.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>An AER_BRIDGE_DESCRIPTOR_FLAGS union that indicates which of the members of the WHEA_AER_BRIDGE_DESCRIPTOR structure can be written to by the operating system. The AER_BRIDGE_DESCRIPTOR_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _AER_BRIDGE_DESCRIPTOR_FLAGS {
  struct {
    USHORT  UncorrectableErrorMaskRW:1;
    USHORT  UncorrectableErrorSeverityRW:1;
    USHORT  CorrectableErrorMaskRW:1;
    USHORT  AdvancedCapsAndControlRW:1;
    USHORT  SecondaryUncorrectableErrorMaskRW:1;
    USHORT  SecondaryUncorrectableErrorSevRW:1;
    USHORT  SecondaryCapsAndControlRW:1;
    USHORT  Reserved:9;
  };
  USHORT  AsUSHORT;
} AER_BRIDGE_DESCRIPTOR_FLAGS, *PAER_BRIDGE_DESCRIPTOR_FLAGS</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="UncorrectableErrorMaskRW"></a><a id="uncorrectableerrormaskrw"></a><a id="UNCORRECTABLEERRORMASKRW"></a><b>UncorrectableErrorMaskRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>UncorrectableErrorMask</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="UncorrectableErrorSeverityRW"></a><a id="uncorrectableerrorseverityrw"></a><a id="UNCORRECTABLEERRORSEVERITYRW"></a><b>UncorrectableErrorSeverityRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>UncorrectableErrorSeverity</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="CorrectableErrorMaskRW"></a><a id="correctableerrormaskrw"></a><a id="CORRECTABLEERRORMASKRW"></a><b>CorrectableErrorMaskRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>CorrectableErrorMask</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="AdvancedCapsAndControlRW"></a><a id="advancedcapsandcontrolrw"></a><a id="ADVANCEDCAPSANDCONTROLRW"></a><b>AdvancedCapsAndControlRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>AdvancedCapsAndControl</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="SecondaryUncorrectableErrorMaskRW"></a><a id="secondaryuncorrectableerrormaskrw"></a><a id="SECONDARYUNCORRECTABLEERRORMASKRW"></a><b>SecondaryUncorrectableErrorMaskRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>SecondaryUncorrectableErrorMask</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="SecondaryUncorrectableErrorSevRW"></a><a id="secondaryuncorrectableerrorsevrw"></a><a id="SECONDARYUNCORRECTABLEERRORSEVRW"></a><b>SecondaryUncorrectableErrorSevRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>SecondaryUncorrectableErrorSev</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="SecondaryCapsAndControlRW"></a><a id="secondarycapsandcontrolrw"></a><a id="SECONDARYCAPSANDCONTROLRW"></a><b>SecondaryCapsAndControlRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>SecondaryCapsAndControl</b> member of the WHEA_AER_BRIDGE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsUSHORT"></a><a id="asushort"></a><a id="ASUSHORT"></a><b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the AER_ROOTPORT_DESCRIPTOR_FLAGS union.</p>
</dd>
</dl>
</dd>

### -field <b>UncorrectableErrorMask</b>

<dd>
<p>The contents of the bridge's Uncorrectable Error Mask register.</p>
</dd>

### -field <b>UncorrectableErrorSeverity</b>

<dd>
<p>The contents of the bridge's Uncorrectable Error Severity register.</p>
</dd>

### -field <b>CorrectableErrorMask</b>

<dd>
<p>The contents of the bridge's Correctable Error Mask register.</p>
</dd>

### -field <b>AdvancedCapsAndControl</b>

<dd>
<p>The contents of the bridge's Advanced Error Capabilities and Control register.</p>
</dd>

### -field <b>SecondaryUncorrectableErrorMask</b>

<dd>
<p>The contents of the bridge's Secondary Uncorrectable Error Mask register.</p>
</dd>

### -field <b>SecondaryUncorrectableErrorSev</b>

<dd>
<p>The contents of the bridge's Secondary Uncorrectable Error Severity register.</p>
</dd>

### -field <b>SecondaryCapsAndControl</b>

<dd>
<p>The contents of the bridge's Secondary Error Capabilities and Control register.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_AER_BRIDGE_DESCRIPTOR structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560595">WHEA_PCI_SLOT_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_AER_BRIDGE_DESCRIPTOR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
