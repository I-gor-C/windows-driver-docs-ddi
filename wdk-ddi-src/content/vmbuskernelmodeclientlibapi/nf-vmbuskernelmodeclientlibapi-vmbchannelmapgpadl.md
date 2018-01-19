---
UID : NF:vmbuskernelmodeclientlibapi.VmbChannelMapGpadl
title : VmbChannelMapGpadl function
author : windows-driver-content
description : The VmbChannelMapGpadl function maps a client-side buffer into server-side physical address space by using a Guest Physical Address Descriptor List (GPADL) number.
old-location : netvista\vmbchannelmapgpadl.htm
old-project : netvista
ms.assetid : A7801EE9-BFDB-4F77-9DA4-A6612F63AD48
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : VmbChannelMapGpadl
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : vmbuskernelmodeclientlibapi.h
req.include-header : VmbusKernelModeClientLibApi.h
req.target-type : Windows
req.target-min-winverclnt : Windows 8.1
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 1.13
req.umdf-ver : 2.0
req.alt-api : VmbChannelMapGpadl
req.alt-loc : VmbusKernelModeClientLibApi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PVIDEO_PORT_AGP_SERVICES, VIDEO_PORT_AGP_SERVICES"
req.product : Windows 10 or later.
---


# VmbChannelMapGpadl function
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>VmbChannelMapGpadl</b>  function maps a client-side buffer into server-side physical address space by using a Guest Physical Address Descriptor List (GPADL) number.

## Syntax

````
NTSTATUS VmbChannelMapGpadl(
  _In_  VMBCHANNEL Channel,
  _In_  UINT32     Flags,
  _In_  UINT32     GpadlHandle,
  _Out_ PMDL       *Mdl
);
````

## Parameters

`Channel`

A handle for a channel.

`Flags`

Flags.  The possible flag values are:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`GpadlHandle`

The GPADL handle of the GPADL to map.

`Mdl`

A pointer to a MDL describing the client buffer. This
buffer is only mapped into physical address space. The caller must take
additional steps to map it into virtual address space.


## Return Value

None

## Remarks

The GPADL must have been pre-established by the client, for instance, by using the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelcreategpadlfrombuffer.md">VmbChannelCreateGpadlFromBuffer</a> function.  

Only a single mapping may exist for any given GPADL at a time.  

You must pair calls to this
function with calls to the <a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelunmapgpadl.md">VmbChannelUnmapGpadl</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** | 1.13 |
| **Minimum UMDF version** | 2.0 |
| **Header** | vmbuskernelmodeclientlibapi.h (include VmbusKernelModeClientLibApi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelcreategpadlfrombuffer.md">VmbChannelCreateGpadlFromBuffer</a>
</dt>
<dt>
<a href="..\vmbuskernelmodeclientlibapi\nf-vmbuskernelmodeclientlibapi-vmbchannelunmapgpadl.md">VmbChannelUnmapGpadl</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20VmbChannelMapGpadl function%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>