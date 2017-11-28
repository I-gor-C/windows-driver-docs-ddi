---
UID: NF.fwpsk.FwpsDereferencevSwitchPacketContext0
title: FwpsDereferencevSwitchPacketContext0
author: windows-driver-content
description: This function is not supported.
old-location: netvista\fwpsdereferencevswitchpacketcontext0.htm
old-project: netvista
ms.assetid: 9A315227-7305-4068-81DE-BD25F733E650
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsDereferencevSwitchPacketContext0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsDereferencevSwitchPacketContext0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FwpsDereferencevSwitchPacketContext0 function



## -description
<p>This function is not supported.</p>


## -syntax

````
void NTAPI FwpsDereferencevSwitchPacketContext0(
   _Inout_ HANDLE packetContext
);
````


## -parameters
<dl>

### -param <i>packetContext</i> 

<dd>
<p>The <b>vSwitchPacketContext</b> value in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a> structure that is passed to callouts during virtual switch transport layer classifies (the FWPS_L2_METADATA_FIELD_VSWITCH_SOURCE_PORT_ID bit will be set in the <b>currentL2MetadataValues</b> member). </p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>The <b>FwpsDereferencevSwitchPacketContext0</b> function releases a reference  that was acquired by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698268">FwpsReferencevSwitchPacketContext0</a> function.</p>

<p>The <b>FwpsDereferencevSwitchPacketContext0</b> function releases a reference  that was acquired by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh698268">FwpsReferencevSwitchPacketContext0</a> function.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552397">FWPS_INCOMING_METADATA_VALUES0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh698268">FwpsReferencevSwitchPacketContext0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsDereferencevSwitchPacketContext0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
