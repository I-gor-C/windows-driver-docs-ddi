---
UID: NF.portcls.IMiniportWavePci.Init
title: IMiniportWavePci::Init
author: windows-driver-content
description: The Init method initializes the WavePci miniport object. Initialization includes verification of the hardware using the resources specified in the resource list.
old-location: audio\iminiportwavepci_init.htm
old-project: audio
ms.assetid: 0796a1a2-1aaa-4e07-a8f1-7a3c895643e7
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IMiniportWavePci, Init, IMiniportWavePci::Init
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
req.alt-api: IMiniportWavePci.Init
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
req.iface: IMiniportWavePci
---

# IMiniportWavePci::Init method



## -description
<p>The <code>Init</code> method initializes the WavePci miniport object. Initialization includes verification of the hardware using the resources specified in the resource list.</p>


## -syntax

````
NTSTATUS Init(
  [in]  PUNKNOWN      UnknownAdapter,
  [in]  PRESOURCELIST ResourceList,
  [in]  PPORTWAVEPCI  Port,
  [out] PSERVICEGROUP *ServiceGroup
);
````


## -parameters
<dl>

### -param <i>UnknownAdapter</i> [in]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of the adapter object whose miniport object is being initialized. For more information, see the following Remarks section.</p>
</dd>

### -param <i>ResourceList</i> [in]

<dd>
<p>Pointer to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> interface of resource list object that is to be supplied to the miniport driver during initialization. After passing this reference to the miniport driver, the port driver is free to examine the contents of the resource list but will not modify the contents of this list. For more information, see the following Remarks section.</p>
</dd>

### -param <i>Port</i> [in]

<dd>
<p>Pointer to the port driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a> interface object. The caller specifies a valid, non-NULL pointer value for this parameter.</p>
</dd>

### -param <i>ServiceGroup</i> [out]

<dd>
<p>Output pointer for the service group. This parameter points to a caller-allocated pointer variable into which the method writes a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a> interface of the miniport driver's service group object. This is the service group that is being registered for interrupt notification. The caller specifies a valid, non-NULL pointer value for this parameter.</p>
</dd>
</dl>

## -returns
<p><code>Init</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>The <i>UnknownAdapter</i> and <i>ResourceList</i> parameters are the same pointer values that the adapter driver earlier passed as parameters to the <b>IPortWavePci</b> object's <b>Init</b> method (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>).</p>

<p>The <i>UnknownAdapter</i>, <i>ResourceList</i>, <i>Port</i>, and <i>ServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>The <i>UnknownAdapter</i> and <i>ResourceList</i> parameters are the same pointer values that the adapter driver earlier passed as parameters to the <b>IPortWavePci</b> object's <b>Init</b> method (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>).</p>

<p>The <i>UnknownAdapter</i>, <i>ResourceList</i>, <i>Port</i>, and <i>ServiceGroup</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536724">IMiniportWavePci</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536905">IPortWavePci</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536943">IPort::Init</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWavePci::Init method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
