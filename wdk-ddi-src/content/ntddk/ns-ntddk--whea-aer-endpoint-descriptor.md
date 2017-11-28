---
UID: NS.ntddk._WHEA_AER_ENDPOINT_DESCRIPTOR
title: WHEA_AER_ENDPOINT_DESCRIPTOR
author: windows-driver-content
description: The WHEA_AER_ENDPOINT_DESCRIPTOR structure describes a PCI Express (PCIe) endpoint error source.
old-location: whea\whea_aer_endpoint_descriptor.htm
old-project: whea
ms.assetid: 2b77853d-2c34-4902-90e3-b9a58d56e88e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_AER_ENDPOINT_DESCRIPTOR, WHEA_AER_ENDPOINT_DESCRIPTOR, *PWHEA_AER_ENDPOINT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_AER_ENDPOINT_DESCRIPTOR
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
req.iface: 
---

# WHEA_AER_ENDPOINT_DESCRIPTOR structure



## -description
<p>The WHEA_AER_ENDPOINT_DESCRIPTOR structure describes a PCI Express (PCIe) endpoint error source.</p>


## -syntax

````
typedef struct _WHEA_AER_ENDPOINT_DESCRIPTOR {
  USHORT                        Type;
  BOOLEAN                       Enabled;
  UCHAR                         Reserved;
  ULONG                         BusNumber;
  WHEA_PCI_SLOT_NUMBER          Slot;
  USHORT                        DeviceControl;
  AER_ENDPOINT_DESCRIPTOR_FLAGS Flags;
  ULONG                         UncorrectableErrorMask;
  ULONG                         UncorrectableErrorSeverity;
  ULONG                         CorrectableErrorMask;
  ULONG                         AdvancedCapsAndControl;
} WHEA_AER_ENDPOINT_DESCRIPTOR, *PWHEA_AER_ENDPOINT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of error source descriptor. This member is always set to WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_AERENDPOINT.</p>
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
<p>The endpoint's bus number.</p>
</dd>

### -field <b>Slot</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560595">WHEA_PCI_SLOT_NUMBER</a> structure that describes the logical PCI slot where the endpoint is located in the system.</p>
</dd>

### -field <b>DeviceControl</b>

<dd>
<p>The contents of the endpoint's Device Control register.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>An AER_ENDPOINT_DESCRIPTOR_FLAGS union that indicates which of the members of the WHEA_AER_ENDPOINT_DESCRIPTOR structure can be written to by the operating system. The AER_ENDPOINT_DESCRIPTOR_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _AER_ENDPOINT_DESCRIPTOR_FLAGS {
  struct {
    USHORT  UncorrectableErrorMaskRW:1;
    USHORT  UncorrectableErrorSeverityRW:1;
    USHORT  CorrectableErrorMaskRW:1;
    USHORT  AdvancedCapsAndControlRW:1;
    USHORT  Reserved:12;
  };
  USHORT  AsUSHORT;
} AER_ENDPOINT_DESCRIPTOR_FLAGS, *PAER_ENDPOINT_DESCRIPTOR_FLAGS</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="UncorrectableErrorMaskRW"></a><a id="uncorrectableerrormaskrw"></a><a id="UNCORRECTABLEERRORMASKRW"></a><b>UncorrectableErrorMaskRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>UncorrectableErrorMask</b> member of the WHEA_AER_ENDPOINT_DESCRIPTOR structure.</p>
</dd>

### -field <a id="UncorrectableErrorSeverityRW"></a><a id="uncorrectableerrorseverityrw"></a><a id="UNCORRECTABLEERRORSEVERITYRW"></a><b>UncorrectableErrorSeverityRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>UncorrectableErrorSeverity</b> member of the WHEA_AER_ENDPOINT_DESCRIPTOR structure.</p>
</dd>

### -field <a id="CorrectableErrorMaskRW"></a><a id="correctableerrormaskrw"></a><a id="CORRECTABLEERRORMASKRW"></a><b>CorrectableErrorMaskRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>CorrectableErrorMask</b> member of the WHEA_AER_ENDPOINT_DESCRIPTOR structure.</p>
</dd>

### -field <a id="AdvancedCapsAndControlRW"></a><a id="advancedcapsandcontrolrw"></a><a id="ADVANCEDCAPSANDCONTROLRW"></a><b>AdvancedCapsAndControlRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>AdvancedCapsAndControl</b> member of the WHEA_AER_ENDPOINT_DESCRIPTOR structure.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsUSHORT"></a><a id="asushort"></a><a id="ASUSHORT"></a><b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the AER_ENDPOINT_DESCRIPTOR_FLAGS union.</p>
</dd>
</dl>
</dd>

### -field <b>UncorrectableErrorMask</b>

<dd>
<p>The contents of the endpoint's Uncorrectable Error Mask register.</p>
</dd>

### -field <b>UncorrectableErrorSeverity</b>

<dd>
<p>The contents of the endpoint's Uncorrectable Error Severity register.</p>
</dd>

### -field <b>CorrectableErrorMask</b>

<dd>
<p>The contents of the endpoint's Correctable Error Mask register.</p>
</dd>

### -field <b>AdvancedCapsAndControl</b>

<dd>
<p>The contents of the endpoint's Advanced Error Capabilities and Control register.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_AER_ENDPOINT_DESCRIPTOR structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_AER_ENDPOINT_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
