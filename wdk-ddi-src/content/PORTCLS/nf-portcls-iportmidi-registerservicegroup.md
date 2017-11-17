---
UID: NF.portcls.IPortMidi.RegisterServiceGroup
title: IPortMidi::RegisterServiceGroup
author: windows-driver-content
description: The RegisterServiceGroup method registers the service group to be used for the IPortMidi::Notify method.
old-location: audio\iportmidi_registerservicegroup.htm
ms.assetid: 8e6b967f-7114-4231-bcfc-23637cd83268
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortMidi.RegisterServiceGroup
req.alt-loc: portcls.h
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
ms.keywords: IPortMidi, RegisterServiceGroup, IPortMidi::RegisterServiceGroup
req.iface: IPortMidi
---

# IPortMidi::RegisterServiceGroup method



## -description
<p>The <code>RegisterServiceGroup</code> method registers the service group to be used for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536893">IPortMidi::Notify</a> method.</p>


## -syntax

````
void RegisterServiceGroup(
  [in] PSERVICEGROUP ServiceGroup
);
````


## -parameters
<dl>

### -param <i>ServiceGroup</i> [in]

<dd>
<p>Pointer to the miniport driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a> object that is being registered.</p>
</dd>
</dl>

## -returns
<p><code>RegisterServiceGroup</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The <i>ServiceGroup</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The <i>ServiceGroup</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536893">IPortMidi::Notify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortMidi::RegisterServiceGroup method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
