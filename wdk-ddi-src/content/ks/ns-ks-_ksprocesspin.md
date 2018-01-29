---
UID : NS:ks._KSPROCESSPIN
title : _KSPROCESSPIN
author : windows-driver-content
description : The KSPROCESSPIN structure describes the process state of a specific pin.
old-location : stream\ksprocesspin.htm
old-project : stream
ms.assetid : a1625eb2-a38b-4517-b873-f33b5ced8705
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSPROCESSPIN, PKSPROCESSPIN, stream.ksprocesspin, ks/KSPROCESSPIN, ks/PKSPROCESSPIN, avstruct_a374bc58-a61f-4d3b-9b20-de14b7cc423f.xml, PKSPROCESSPIN structure pointer [Streaming Media Devices], *PKSPROCESSPIN, KSPROCESSPIN structure [Streaming Media Devices], _KSPROCESSPIN
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PKSPROCESSPIN, KSPROCESSPIN"
---

# _KSPROCESSPIN structure
The KSPROCESSPIN structure describes the process state of a specific pin.

## Syntax
````
typedef struct _KSPROCESSPIN {
  PKSPIN            Pin;
  PKSSTREAM_POINTER StreamPointer;
  PKSPROCESSPIN     InPlaceCounterpart;
  PKSPROCESSPIN     DelegateBranch;
  PKSPROCESSPIN     CopySource;
  PVOID             Data;
  ULONG             BytesAvailable;
  ULONG             BytesUsed;
  ULONG             Flags;
  BOOLEAN           Terminate;
} KSPROCESSPIN, *PKSPROCESSPIN;
````

## Members


## Remarks
The KSPROCESSPIN structure is used in the <a href="https://msdn.microsoft.com/e56c5102-7ea6-4687-ae5e-1550db9500f0">filter-centric processing</a> model. You can use this structure to access data on a specific input pin or to write out processed data to an output pin.

Only filter-centric clients use process pins. Further, process pins that have a non-<b>NULL</b><b>DelegateBranch</b> or a non-<b>NULL</b><b>CopySource</b> typically are not of concern to the client. The splitter automatically handles process pins with these pointers.

Most clients are concerned with the members <b>Pin</b>, <b>Data</b>, <b>BytesAvailable</b>, <b>BytesUsed</b>, <b>Flags</b>, and <b>Terminate</b>. Data can be read from the stream or written into the stream through the <b>Data</b> member; <b>BytesAvailable</b> tells the client how many bytes of data are available in the current data frame (buffer) that <b>Data</b> points to. As the client minidriver reads from or writes to the stream, <b>BytesUsed</b> should be updated to reflect how many bytes of data have been consumed. The <b>Terminate</b> flag can be set if the minidriver is done with the current frame despite the fact that <b>BytesUsed</b> is not equal to <b>BytesAvailable</b>. After the minidriver exits the processing dispatch, pointers are advanced, and frames are completed as appropriate.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\ns-ks-ksstream_header.md">KSSTREAM_HEADER</a>

<a href="..\ks\ns-ks-_ksstream_pointer.md">KSSTREAM_POINTER</a>

<a href="..\ks\ns-ks-_kspin.md">KSPIN</a>

<a href="..\ks\ns-ks-_ksprocesspin_indexentry.md">KSPROCESSPIN_INDEXENTRY</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROCESSPIN structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>