---
UID: NS.ntddk._PCI_EXPRESS_PME_REQUESTOR_ID
title: PCI_EXPRESS_PME_REQUESTOR_ID
author: windows-driver-content
description: The PCI_EXPRESS_PME_REQUESTOR_ID structure describes the identifier of the requester of a power management event (PME).
old-location: pci\pci_express_pme_requestor_id.htm
ms.assetid: 2305ffbd-22c8-4f63-bbe4-fd297bf98e39
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: PCI
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCI_EXPRESS_PME_REQUESTOR_ID
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
ms.keywords: PCI_EXPRESS_PME_REQUESTOR_ID, PCI_EXPRESS_PME_REQUESTOR_ID, *PPCI_EXPRESS_PME_REQUESTOR_ID
req.iface: 
---

# PCI_EXPRESS_PME_REQUESTOR_ID structure



## -description
<p>The PCI_EXPRESS_PME_REQUESTOR_ID structure describes the identifier of the requester of a power management event (PME).</p>


## -syntax

````
typedef union _PCI_EXPRESS_PME_REQUESTOR_ID {
  struct {
    USHORT FunctionNumber  :3;
    USHORT DeviceNumber  :5;
    USHORT BusNumber  :3;
  };
  USHORT AsUSHORT;
} PCI_EXPRESS_PME_REQUESTOR_ID, *PPCI_EXPRESS_PME_REQUESTOR_ID;
````


## -struct-fields
<dl>

### -field <b>FunctionNumber</b>

<dd>
<p>The function number of the requester.</p>
</dd>

### -field <b>DeviceNumber</b>

<dd>
<p>The device number of the requester.</p>
</dd>

### -field <b>BusNumber</b>

<dd>
<p>The bus number of the requester.</p>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>A USHORT representation of the contents of the PCI_EXPRESS_PME_REQUESTOR_ID structure.</p>
</dd>
</dl>

## -remarks
<p>The PCI_EXPRESS_PME_REQUESTOR_ID structure is available in Windows Server 2008 and later versions of Windows.</p>

<p>A PCI_EXPRESS_PME_REQUESTOR_ID structure is contained in the <b>PMERequestorId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537477">PCI_EXPRESS_ROOT_STATUS_REGISTER</a> structure.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537477">PCI_EXPRESS_ROOT_STATUS_REGISTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20PCI_EXPRESS_PME_REQUESTOR_ID union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
