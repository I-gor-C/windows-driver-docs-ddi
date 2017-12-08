---
UID: NC.ks.PFNKSDEVICEIRP
title: PFNKSDEVICEIRP
author: windows-driver-content
description: AVStream calls a minidriver's AVStrMiniDeviceQueryInterface routine when it receives an IRP_MN_QUERY_INTERFACE.
old-location: stream\avstrminidevicequeryinterface.htm
old-project: stream
ms.assetid: 301c206d-5875-4db7-b8ec-73c32e9533f0
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniDeviceQueryInterface
req.alt-loc: ks.h
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
---

# PFNKSDEVICEIRP callback



## -description
AVStream calls a minidriver's <i>AVStrMiniDeviceQueryInterface</i> routine when it receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>.


## -prototype

````
PFNKSDEVICEIRP AVStrMiniDeviceQueryInterface;

NTSTATUS AVStrMiniDeviceQueryInterface(
  _In_ PKSDEVICE Device,
  _In_ PIRP      Irp
)
{ ... }
````


## -parameters

### -param Device [in]

Pointer to the <a href="stream.ksdevice">KSDEVICE</a> structure that received the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>.

### -param Irp [in]

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a> issued by <i>Device</i>.

## -returns
Your driver should return STATUS_SUCCESS or an appropriate error status.

## -remarks
A driver or system component sends this IRP to get information about an interface exported by your driver. For more information about the IRP, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>.

The minidriver specifies this routine's address in the <b>QueryInterface</b> member of its <a href="stream.ksdevice_dispatch">KSDEVICE_DISPATCH</a> structure.

This routine is optional.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksdevice_dispatch">KSDEVICE_DISPATCH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551687">IRP_MN_QUERY_INTERFACE</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniDeviceQueryInterface routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
