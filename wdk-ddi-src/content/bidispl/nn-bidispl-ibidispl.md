---
UID : NN:bidispl.IBidiSpl
title : IBidiSpl
author : windows-driver-content
description : The IBidiSpl interface allows an application or other objects to send a single bidi request or a list of bidi requests.
old-location : print\ibidispl.htm
old-project : print
ms.assetid : 7e4a30b2-ac3a-475a-b818-455cdb7a91bf
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.ibidispl, IBidiSpl interface [Print Devices], IBidiSpl interface [Print Devices], described, IBidiSpl, bidispl/IBidiSpl, _win32_IBidiSpl, gdi.ibidispl
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : bidispl.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows XP
req.target-min-winversvr : Windows Server 2003
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : bidispl.h
req.dll : Bidispl.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PMPEG2_TRANSPORT_STRIDE, MPEG2_TRANSPORT_STRIDE"
---

# IBidiSpl interface

The <b>IBidiSpl</b> interface allows an application or other objects to send a single bidi request or a list of bidi requests.

## Methods

<p>The <b>IBidiSpl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [bidispl.IBidiSpl.BindDevice](nf-bidispl-ibidispl-binddevice.md) | The IBidiSpl::BindDevice method binds a printer to a bidi request. This method is similar to the OpenPrinter function. |
| [bidispl.IBidiSpl.MultiSendRecv](nf-bidispl-ibidispl-multisendrecv.md) | The IBidiSpl::MultiSendRecv method sends a list of bidi requests. |
| [bidispl.IBidiSpl.SendRecv](nf-bidispl-ibidispl-sendrecv.md) | The IBidiSpl::SendRecv method sends a bidi request to the printer. |
| [bidispl.IBidiSpl.UnbindDevice](nf-bidispl-ibidispl-unbinddevice.md) | The IBidiSpl::UnbindDevice method unbinds a printer from a bidi request. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | bidispl.h |
| **DLL** | Bidispl.dll |

## See Also

<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>

<a href="..\bidispl\nn-bidispl-ibidirequestcontainer.md">IBidiSpl</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IBidiSpl interface%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>