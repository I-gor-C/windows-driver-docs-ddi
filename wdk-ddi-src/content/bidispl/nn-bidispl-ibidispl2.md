---
UID: NN:bidispl.IBidiSpl2
title: IBidiSpl2
author: windows-driver-content
description: The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.
old-location: print\ibidispl2.htm
old-project: print
ms.assetid: 90e8a390-7d30-4bcf-8c81-438c86529ceb
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IBidiSpl2, IBidiSpl2 interface [Print Devices], IBidiSpl2 interface [Print Devices], described, _win32_IBidiSpl2, bidispl/IBidiSpl2, gdi.ibidispl2, print.ibidispl2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: Bidispl.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Bidispl.h
api_name:
-	IBidiSpl2
product: Windows
targetos: Windows
req.typenames: MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE
---

# IBidiSpl2 interface

The <b>IBidiSpl2</b> interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.

## Methods

<p>The <b>IBidiSpl2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IBidiSpl2::BindDevice](nf-bidispl-ibidispl2-binddevice.md) | The BindDevice method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the OpenPrinter function. |
| [IBidiSpl2::SendRecvXMLStream](nf-bidispl-ibidispl2-sendrecvxmlstream.md) | The SendRecvXMLStream method sends a bidirectional printer communication request and receives the response as IStream objects formatted in accordance with the Bidirectional Communication Schemas. |
| [IBidiSpl2::SendRecvXMLString](nf-bidispl-ibidispl2-sendrecvxmlstring.md) | The SendRecvXMLString method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the Bidirectional Communication Schemas. |
| [IBidiSpl2::UnbindDevice](nf-bidispl-ibidispl2-unbinddevice.md) | The UnbindDevice method releases a printer from a bidirectional printer communication (bidi communication) request. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows Vista Windows Vista |
| **Target Platform** | Windows |
| **Header** | bidispl.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>



<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>



<a href="https://msdn.microsoft.com/42b5e6cf-b434-4734-86f3-b3b9d15ea468">Print Spooler Components</a>