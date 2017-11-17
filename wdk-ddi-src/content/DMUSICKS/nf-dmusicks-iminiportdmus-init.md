---
UID: NF.dmusicks.IMiniportDMus.Init
title: IMiniportDMus::Init
author: windows-driver-content
description: The Init method initializes the DMus miniport object.
old-location: audio\iminiportdmus_init.htm
ms.assetid: 08111f70-d0cc-4abc-8bcd-86683af3eb32
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: dmusicks.h
req.include-header: Dmusicks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportDMus.Init
req.alt-loc: dmusicks.h
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
ms.keywords: IMiniportDMus, Init, IMiniportDMus::Init
req.iface: IMiniportDMus
---

# IMiniportDMus::Init method



## -description
<p>The <code>Init</code> method initializes the DMus miniport object.</p>


## -syntax

````
NTSTATUS Init(
  [in, optional] PUNKNOWN      pUnknownAdapter,
  [in]           PRESOURCELIST pResourceList,
  [in]           PPORTDMUS     pPort,
  [out]          PSERVICEGROUP *ppServiceGroup
);
````


## -parameters
<dl>

### -param <i>pUnknownAdapter</i> [in, optional]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of the adapter object whose miniport object is being initialized. This parameter is optional and can be specified as <b>NULL</b>. For more information, see the following Remarks section.</p>
</dd>

### -param <i>pResourceList</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> object that contains the adapter's resource list. After passing this reference to the miniport driver, the port driver is free to examine the contents of the resource list but will not modify the contents of this list.</p>
</dd>

### -param <i>pPort</i> [in]

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a> object that provides the port driver's callback interface.</p>
</dd>

### -param <i>ppServiceGroup</i> [out]

<dd>
<p>Output pointer for the service group. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a> interface of the miniport driver's service group object. This is the service group that this miniport driver wants to have used for calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536880">IPortDMus::Notify</a>.</p>
</dd>
</dl>

## -returns
<p><code>Init</code> returns S_OK if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The <i>pUnknownAdapter</i> parameter is optional:</p>

<p>If <i>pUnknownAdapter</i> is non-<b>NULL</b>, the <code>Init</code> method queries the <i>pUnknownAdapter</i> object for its <a href="https://msdn.microsoft.com/library/windows/hardware/ff536590">IInterruptSync</a> interface.</p>

<p>If <i>pUnknownAdapter</i> is <b>NULL</b>, the <code>Init</code> method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff537713">PcNewInterruptSync</a> to create a new <b>IInterruptSync</b> object. In this case, the resource list that <i>pResourceList</i> points to supplies the interrupt resource that the new <b>IInterruptSync</b> object uses.</p>

<p>In either case, the <code>Init</code> method and calls the <b>RegisterServiceRoutine</b> method on the <b>IInterruptSync</b> object in order to add the miniport driver's interrupt service routine (ISR) to the list of ISRs. When the adapter driver later frees the port object, the port driver releases its reference to the <b>IInterruptSync</b> object.</p>

<p>The <i>pUnknownAdapter</i> and <i>pResourceList</i> parameters are the same pointer values that the adapter driver earlier passed as parameters to the <b>IPortDMus</b> object's <code>Init</code> method (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>).</p>

<p>The <i>pUnknownAdapter</i>, <i>pResourceList</i>, <i>pPort</i>, and <i>ppServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The <i>pUnknownAdapter</i> parameter is optional:</p>

<p>If <i>pUnknownAdapter</i> is non-<b>NULL</b>, the <code>Init</code> method queries the <i>pUnknownAdapter</i> object for its <a href="https://msdn.microsoft.com/library/windows/hardware/ff536590">IInterruptSync</a> interface.</p>

<p>If <i>pUnknownAdapter</i> is <b>NULL</b>, the <code>Init</code> method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff537713">PcNewInterruptSync</a> to create a new <b>IInterruptSync</b> object. In this case, the resource list that <i>pResourceList</i> points to supplies the interrupt resource that the new <b>IInterruptSync</b> object uses.</p>

<p>In either case, the <code>Init</code> method and calls the <b>RegisterServiceRoutine</b> method on the <b>IInterruptSync</b> object in order to add the miniport driver's interrupt service routine (ISR) to the list of ISRs. When the adapter driver later frees the port object, the port driver releases its reference to the <b>IInterruptSync</b> object.</p>

<p>The <i>pUnknownAdapter</i> and <i>pResourceList</i> parameters are the same pointer values that the adapter driver earlier passed as parameters to the <b>IPortDMus</b> object's <code>Init</code> method (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>).</p>

<p>The <i>pUnknownAdapter</i>, <i>pResourceList</i>, <i>pPort</i>, and <i>ppServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dmusicks.h (include Dmusicks.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536879">IPortDMus</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536880">IPortDMus::Notify</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536590">IInterruptSync</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537713">PcNewInterruptSync</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportDMus::Init method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
