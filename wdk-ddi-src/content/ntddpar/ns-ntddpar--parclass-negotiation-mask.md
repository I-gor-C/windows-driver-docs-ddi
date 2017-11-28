---
UID: NS.ntddpar._PARCLASS_NEGOTIATION_MASK
title: PARCLASS_NEGOTIATION_MASK
author: windows-driver-content
description: The PARCLASS_NEGOTIATION_MASK structure specifies the read and write protocols that a driver selects for a parallel device.
old-location: parports\parclass_negotiation_mask.htm
old-project: parports
ms.assetid: 6d246ec3-47f1-46da-8ac4-f073f91c0d44
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PARCLASS_NEGOTIATION_MASK, PARCLASS_NEGOTIATION_MASK, *PPARCLASS_NEGOTIATION_MASK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddpar.h
req.include-header: Ntddpar.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARCLASS_NEGOTIATION_MASK
req.alt-loc: ntddpar.h
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

# PARCLASS_NEGOTIATION_MASK structure



## -description
<p>The PARCLASS_NEGOTIATION_MASK structure specifies the read and write protocols that a driver selects for a parallel device.</p>


## -syntax

````
typedef struct _PARCLASS_NEGOTIATION_MASK {
  USHORT usReadMask;
  USHORT usWriteMask;
} PARCLASS_NEGOTIATION_MASK, *PPARCLASS_NEGOTIATION_MASK;
````


## -struct-fields
<dl>

### -field <b>usReadMask</b>

<dd>
<p>Specifies the read protocols. For read and write protocol values, see the constants that are defined in <i>ntddpar.h</i> (from NONE to ECP_ANY).</p>
</dd>

### -field <b>usWriteMask</b>

<dd>
<p>Specifies the write protocols.</p>
</dd>
</dl>

## -remarks
<p>A client specifies a set of requested protocols by setting a bitwise OR of the constants that represent each protocol. The system-supplied bus driver for parallel ports selects the fastest protocol that it supports from among those specified by the client. </p>

<p>For more information, see <a href="NULL">Setting and Clearing a Communication Mode for a Parallel Device</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddpar.h (include Ntddpar.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543975">IOCTL_IEEE1284_GET_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543978">IOCTL_IEEE1284_NEGOTIATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544061">IOCTL_PAR_GET_DEFAULT_MODES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544365">PDETERMINE_IEEE_MODES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544386">PNEGOTIATE_IEEE_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PARCLASS_NEGOTIATION_MASK structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
