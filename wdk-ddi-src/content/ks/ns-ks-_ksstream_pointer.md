---
UID : NS:ks._KSSTREAM_POINTER
title : _KSSTREAM_POINTER
author : windows-driver-content
description : The KSSTREAM_POINTER structure is the basic AVStream pointer into a stream.
old-location : stream\ksstream_pointer.htm
old-project : stream
ms.assetid : 31cdb264-89a1-48dc-af0c-b18d4f077d0f
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _KSSTREAM_POINTER, *PKSSTREAM_POINTER, KSSTREAM_POINTER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSSTREAM_POINTER
req.alt-loc : ks.h
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
req.typenames : "*PKSSTREAM_POINTER, KSSTREAM_POINTER"
---

# _KSSTREAM_POINTER structure
The KSSTREAM_POINTER structure is the basic AVStream pointer into a stream.

## Syntax
````
typedef struct _KSSTREAM_POINTER {
  PVOID                    Context;
  PKSPIN                   Pin;
  PKSSTREAM_HEADER         StreamHeader;
  PKSSTREAM_POINTER_OFFSET Offset;
  KSSTREAM_POINTER_OFFSET  OffsetIn;
  KSSTREAM_POINTER_OFFSET  OffsetOut;
} KSSTREAM_POINTER, *PKSSTREAM_POINTER;
````

## Members


    ## Remarks
        A queue object for a stream has at minimum one hard-defined stream pointer: the leading-edge stream pointer. For more information, see <a href="https://msdn.microsoft.com/73ab974f-8034-421f-980a-2393d84ec54c">Leading and Trailing Edge Stream Pointers</a>.

For general information about stream pointers, see <a href="https://msdn.microsoft.com/4bac68a0-34d2-431a-9ed9-8a42751a736f">Stream Pointers</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ks\ns-ks-ksstream_header.md">KSSTREAM_HEADER</a>
</dt>
<dt>
<a href="..\ks\ns-ks-_ksstream_pointer_offset.md">KSSTREAM_POINTER_OFFSET</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerclone.md">KsStreamPointerClone</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerdelete.md">KsStreamPointerDelete</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerlock.md">KsStreamPointerLock</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerunlock.md">KsStreamPointerUnlock</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointeradvance.md">KsStreamPointerAdvance</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointeradvanceoffsets.md">KsStreamPointerAdvanceOffsets</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointeradvanceoffsetsandunlock.md">KsStreamPointerAdvanceOffsetsAndUnlock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSSTREAM_POINTER structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>