---
UID: NN:bidispl.IBidiSpl
title: IBidiSpl
author: windows-driver-content
description: The IBidiSpl interface allows an application or other objects to send a single bidi request or a list of bidi requests.
old-location: print\ibidispl.htm
old-project: print
ms.assetid: 7e4a30b2-ac3a-475a-b818-455cdb7a91bf
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IBidiSpl, IBidiSpl interface [Print Devices], IBidiSpl interface [Print Devices], described, _win32_IBidiSpl, bidispl/IBidiSpl, gdi.ibidispl, print.ibidispl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: bidispl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP
req.target-min-winversvr: Windows Server 2003
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
-	IBidiSpl
product: Windows
targetos: Windows
req.typenames: MPEG2_TRANSPORT_STRIDE, *PMPEG2_TRANSPORT_STRIDE
---

# IBidiSpl interface

The <b>IBidiSpl</b> interface allows an application or other objects to send a single bidi request or a list of bidi requests.

## Methods

<p>The <b>IBidiSpl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IBidiSpl::BindDevice](nf-bidispl-ibidispl-binddevice.md) | The BindDevice method binds a printer to a bidi request. This method is similar to the OpenPrinter function. |
| [IBidiSpl::MultiSendRecv](nf-bidispl-ibidispl-multisendrecv.md) | The MultiSendRecv method sends a list of bidi requests. |
| [IBidiSpl::SendRecv](nf-bidispl-ibidispl-sendrecv.md) | The SendRecv method sends a bidi request to the printer. |
| [IBidiSpl::UnbindDevice](nf-bidispl-ibidispl-unbinddevice.md) | The UnbindDevice method unbinds a printer from a bidi request. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Windows XP |
| **Target Platform** | Windows |
| **Header** | bidispl.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff545163">Bidirectional Communication Interfaces</a>



<a href="https://msdn.microsoft.com/b15b1aff-623e-4159-ab0f-ce386a1377eb">Bidirectional Communication Schema</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dd144980">IBidiSpl</a>