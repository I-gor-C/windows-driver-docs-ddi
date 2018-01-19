---
UID : NE:avcstrm._AVCSTRM_FUNCTION
title : _AVCSTRM_FUNCTION
author : windows-driver-content
description : The AVCSTRM_FUNCTION enumeration defines the functionality exposed by the avcstrm.sys driver.
old-location : stream\avcstrm_function.htm
old-project : stream
ms.assetid : 0dacc4b0-003f-4c73-8705-1c1e86ce357c
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _AVCSTRM_FUNCTION, AVCSTRM_FUNCTION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : avcstrm.h
req.include-header : Avcstrm.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : AVCSTRM_FUNCTION
req.alt-loc : avcstrm.h
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
req.typenames : AVCSTRM_FUNCTION
---

# _AVCSTRM_FUNCTION Enumeration
The AVCSTRM_FUNCTION enumeration defines the functionality exposed by the <i>avcstrm.sys</i> driver.

## Syntax
````
typedef enum _AVCSTRM_FUNCTION { 
  AVCSTRM_READ             = 0,
  AVCSTRM_WRITE            = 1,
  AVCSTRM_ABORT_STREAMING  = 2,
  AVCSTRM_OPEN             = 0x100,
  AVCSTRM_CLOSE            = 0x101,
  AVCSTRM_GET_STATE        = 0x102,
  AVCSTRM_SET_STATE        = 0x103,
  AVCSTRM_GET_PROPERTY     = 0x104,
  AVCSTRM_SET_PROPERTY     = 0x105
} AVCSTRM_FUNCTION;
````

## Constants

<table>

<tr>
<td>AVCSTRM_ABORT_STREAMING</td>
<td>Abort streaming. This cancels <i>all</i> streaming IRPs. To cancel an individual IRP, use <a href="..\wdm\nf-wdm-iocancelirp.md">IoCancelIrp</a>.</td>
</tr>

<tr>
<td>AVCSTRM_CLOSE</td>
<td>Close a stream and free any resources allocated for the stream.</td>
</tr>

<tr>
<td>AVCSTRM_GET_PROPERTY</td>
<td>Get stream property. This function is not implemented.</td>
</tr>

<tr>
<td>AVCSTRM_GET_STATE</td>
<td>Obtain the stream state.</td>
</tr>

<tr>
<td>AVCSTRM_OPEN</td>
<td>Open a stream in a specific format.</td>
</tr>

<tr>
<td>AVCSTRM_READ</td>
<td>Read data from a stream.</td>
</tr>

<tr>
<td>AVCSTRM_SET_PROPERTY</td>
<td>Set stream property. This function is not implemented.</td>
</tr>

<tr>
<td>AVCSTRM_SET_STATE</td>
<td>Place the  stream into a new state.</td>
</tr>

<tr>
<td>AVCSTRM_WRITE</td>
<td>Write data to a stream.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | avcstrm.h (include Avcstrm.h) |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554130">AVCSTRM_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554135">AVCSTRM_WRITE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554107">AVCSTRM_ABORT_STREAMING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554125">AVCSTRM_OPEN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554110">AVCSTRM_CLOSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554124">AVCSTRM_GET_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554134">AVCSTRM_SET_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554121">AVCSTRM_GET_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554132">AVCSTRM_SET_PROPERTY</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVCSTRM_FUNCTION enumeration%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>