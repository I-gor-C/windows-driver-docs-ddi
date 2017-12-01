---
UID: NF.portcls.IMiniportWaveRT.Init
title: IMiniportWaveRT::Init
author: windows-driver-content
description: The Init method initializes the WaveRT miniport driver object.
old-location: audio\iminiportwavert_init.htm
old-project: audio
ms.assetid: f25be064-6ad4-42e8-87a5-188978d093fb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IMiniportWaveRT, Init, IMiniportWaveRT::Init
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IMiniportWaveRT.Init
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
req.irql: Passive level.
req.iface: IMiniportWaveRT
---

# IMiniportWaveRT::Init method



## -description
<p>The <code>Init</code> method initializes the <a href="NULL">WaveRT miniport driver</a> object.</p>


## -syntax

````
NTSTATUS Init(
  [in] PUNKNOWN      UnknownAdapter,
  [in] PRESOURCELIST ResourceList,
  [in] PPORTWAVERT   Port
);
````


## -parameters
<dl>

### -param <i>UnknownAdapter</i> [in]

<dd>
<p>Pointer to the <b>IUnknown</b> interface of the adapter driver object whose miniport driver object is being initialized.</p>
</dd>

### -param <i>ResourceList</i> [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iresourcelist.md">IResourceList</a> interface of a resource-list object. This object specifies the list of hardware resources that the adapter driver has allocated to the miniport driver. The WaveRT port driver can examine the contents of the resource list, but it does not modify the list.</p>
</dd>

### -param <i>Port</i> [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iportwavert.md">IPortWaveRT</a> interface of the WaveRT port driver. The caller specifies a valid, non-NULL pointer value for this parameter.</p>
</dd>
</dl>

## -returns
<p><code>Init</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error status code.</p>

## -remarks
<p>For more information about the <i>ResourceList</i> parameter, see the <a href="audio.iport_init">IPort::Init </a> topic. The <i>ResourceList</i> and <i>Port</i> parameters follow the reference-counting conventions for COM objects.</p>

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
<p>Available in Windows Vista and later Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Passive level.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iminiportwavert.md">IMiniportWaveRT</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iportwavert.md">IPortWaveRT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IMiniportWaveRT::Init method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
