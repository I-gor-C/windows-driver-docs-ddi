---
UID: NN:bidispl.IBidiSpl2
title: IBidiSpl2
author: windows-driver-content
description: The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.
old-location: print\ibidispl2.htm
old-project: print
ms.assetid: 90e8a390-7d30-4bcf-8c81-438c86529ceb
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: print.ibidispl2, IBidiSpl2 interface [Print Devices], IBidiSpl2 interface [Print Devices], described, IBidiSpl2, bidispl/IBidiSpl2, _win32_IBidiSpl2, gdi.ibidispl2
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
req.lib: bidispl.h
req.dll: Bidispl.dll
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Bidispl.h
apiname:
-	IBidiSpl2
product: Windows
targetos: Windows
req.typenames: "*PMPEG2_TRANSPORT_STRIDE, MPEG2_TRANSPORT_STRIDE"
---

# IBidiSpl2 interface

The <b>IBidiSpl2</b> interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.

## Methods

<p>The <b>IBidiSpl2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [bidispl.IBidiSpl2.BindDevice](nf-bidispl-ibidispl2-binddevice.md) | The IBidiSpl2::BindDevice method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the OpenPrinter function. |
| [bidispl.IBidiSpl2.SendRecvXMLStream](nf-bidispl-ibidispl2-sendrecvxmlstream.md) | The IBidiSpl2::SendRecvXMLStream method sends a bidirectional printer communication request and receives the response as IStream objects formatted in accordance with the Bidirectional Communication Schemas. |
| [bidispl.IBidiSpl2.SendRecvXMLString](nf-bidispl-ibidispl2-sendrecvxmlstring.md) | The IBidiSpl2::SendRecvXMLString method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the Bidirectional Communication Schemas. |
| [bidispl.IBidiSpl2.UnbindDevice](nf-bidispl-ibidispl2-unbinddevice.md) | The IBidiSpl2::UnbindDevice method releases a printer from a bidirectional printer communication (bidi communication) request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows Vista Windows Vista |
| **Target Platform** | Windows |
| **Header** | bidispl.h |

## See Also

<a href="https://msdn.microsoft.com/42b5e6cf-b434-4734-86f3-b3b9d15ea468">Print Spooler Components</a>

<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl2 interface%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>