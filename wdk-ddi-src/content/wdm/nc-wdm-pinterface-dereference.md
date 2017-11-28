---
UID: NC.wdm.PINTERFACE_DEREFERENCE
title: PINTERFACE_DEREFERENCE
author: windows-driver-content
description: The InterfaceDereference routine decrements the reference count on a driver-defined interface.
old-location: kernel\interfacedereference.htm
old-project: kernel
ms.assetid: ed23d7fb-0fff-4c04-9291-90e7323f3e6f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: InterfaceDereference
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# PINTERFACE_DEREFERENCE callback



## -description
<p>The <i>InterfaceDereference</i> routine decrements the reference count on a driver-defined interface.</p>


## -prototype

````
PINTERFACE_DEREFERENCE InterfaceDereference;

VOID InterfaceDereference(
  _In_ PVOID Context
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A pointer to interface-specific context information. The caller passes the value that is passed as the <b>Context</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a> structure for the interface.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>You can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a> routine to increment the reference count for the interface.</p>

<p>The driver that imports the interface is responsible for calling the <i>InterfaceDereference</i> routine to decrement the reference count after the driver is no longer using the interface.  For example, a driver that requests a pointer to the interface by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request calls <i>InterfaceDereference</i>. Also, a driver that receives a pointer to the interface to another driver must call <i>InterfaceDereference</i>.</p>

<p>You can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a> routine to increment the reference count for the interface.</p>

<p>The driver that imports the interface is responsible for calling the <i>InterfaceDereference</i> routine to decrement the reference count after the driver is no longer using the interface.  For example, a driver that requests a pointer to the interface by sending an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> request calls <i>InterfaceDereference</i>. Also, a driver that receives a pointer to the interface to another driver must call <i>InterfaceDereference</i>.</p>

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
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547833">InterfaceReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20InterfaceDereference routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
