---
UID: NF.portcls.IMiniportMidi.Init
title: IMiniportMidi::Init
author: windows-driver-content
description: The Init method initializes the MIDI miniport object.
old-location: audio\iminiportmidi_init.htm
old-project: audio
ms.assetid: 2afec522-5a40-4db2-9f37-ee7a9b64e823
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportMidi, Init, IMiniportMidi::Init
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportMidi.Init
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
req.iface: IMiniportMidi
---

# IMiniportMidi::Init method



## -description
<p>The <code>Init</code> method initializes the MIDI miniport object.</p>


## -syntax

````
NTSTATUS Init(
  [in]  PUNKNOWN      UnknownAdapter,
  [in]  PRESOURCELIST ResourceList,
  [in]  PPORTMIDI     Port,
  [out] PSERVICEGROUP *ServiceGroup
);
````


## -parameters
<dl>

### -param UnknownAdapter [in]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of the adapter object whose miniport object is being initialized. This parameter is optional and can be specified as <b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param ResourceList [in]

<dd>
<p>Pointer to <a href="..\portcls\nn-portcls-iresourcelist.md">IResourceList</a> interface of the resource list object that is to be supplied to the miniport driver during initialization. After passing this reference to the miniport driver, the port driver is free to examine the contents of the resource list but will not modify the contents of this list. For more information, see the following Remarks section.</p>
</dd>

### -param Port [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iportmidi.md">IPortMidi</a> object that is bound to this miniport object. The caller specifies a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param ServiceGroup [out]

<dd>
<p>Output pointer for the service group. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a> interface of the miniport driver's service group object. This is the service group that is being registered for interrupt notification. The caller specifies a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>
</dl>

## -returns
<p><code>Init</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The <i>UnknownAdapter</i> parameter is optional:</p>

<p>If <i>UnknownAdapter</i> is non-<b>NULL</b>, the <code>Init</code> method queries the <i>UnknownAdapter</i> object for its <a href="..\portcls\nn-portcls-iinterruptsync.md">IInterruptSync</a> interface.</p>

<p>If <i>UnknownAdapter</i> is <b>NULL</b>, the <code>Init</code> method calls <a href="..\portcls\nf-portcls-pcnewinterruptsync.md">PcNewInterruptSync</a> to create a new <b>IInterruptSync</b> object. In this case, the resource list that <i>ResourceList</i> points to supplies the interrupt resource that the new <b>IInterruptSync</b> object uses.</p>

<p>In either case, the <code>Init</code> method and calls the <b>RegisterServiceRoutine</b> method on the <b>IInterruptSync</b> object in order to add the miniport driver's interrupt service routine (ISR) to the list of interrupt sync routines. When the adapter driver later frees the port object, the port driver releases its reference to the <b>IInterruptSync</b> object.</p>

<p>The <i>UnknownAdapter</i> and <i>ResourceList</i> parameters are the same pointer values that the adapter driver earlier passed as parameters to the <b>IPortMidi</b> object's <b>Init</b> method (see <a href="audio.iport_init">IPort::Init</a>).</p>

<p>The <i>UnknownAdapter</i>, <i>ResourceList</i>, <i>Port</i>, and <i>ServiceGroup</i> parameters follow the <a href="https://msdn.microsoft.com/e6b19110-37e2-4d23-a528-6393c12ab650">reference-counting conventions for COM objects</a>.</p>

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
<a href="..\portcls\nn-portcls-iminiportmidi.md">IMiniportMidi</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iresourcelist.md">IResourceList</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iportmidi.md">IPortMidi</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iinterruptsync.md">IInterruptSync</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcnewinterruptsync.md">PcNewInterruptSync</a>
</dt>
<dt>
<a href="audio.iport_init">IPort::Init</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportMidi::Init method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
