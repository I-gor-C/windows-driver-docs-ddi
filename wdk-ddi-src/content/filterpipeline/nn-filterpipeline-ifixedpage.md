---
UID : NN:filterpipeline.IFixedPage
title : IFixedPage
author : windows-driver-content
description : A filter uses the IFixedPage interface to work with fixed pages in an XPS document.
old-location : print\ifixedpage.htm
old-project : print
ms.assetid : e9e309ed-42e5-40cc-a230-6ca001f9fb1b
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IXpsPartIterator, IXpsPartIterator::Reset, Reset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IFixedPage
req.alt-loc : filterpipeline.h
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
req.typenames : EXpsFontRestriction
---

# IFixedPage interface

A filter uses the <b>IFixedPage</b> interface to work with fixed pages in an XPS document.

## Methods

<p>The <b>IFixedPage</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IFixedPage.DeleteResource](nf-filterpipeline-ifixedpage-deleteresource.md) | The DeleteResource method deletes a resource that is associated with the page. |
| [filterpipeline.IFixedPage.GetPagePart](nf-filterpipeline-ifixedpage-getpagepart.md) | The GetPagePart method gets the images, thumbnails, fonts, and so on in a page by using the URI. |
| [filterpipeline.IFixedPage.GetPrintTicket](nf-filterpipeline-ifixedpage-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed page. |
| [filterpipeline.IFixedPage.GetWriteStream](nf-filterpipeline-ifixedpage-getwritestream.md) | The GetWriteStream method retrieves the stream object to write page markup to read . You can use this stream to change page markup. |
| [filterpipeline.IFixedPage.GetXpsPartIterator](nf-filterpipeline-ifixedpage-getxpspartiterator.md) | The GetXpsPartIterator method gets an iterator to enumerate all of the parts that are associated with the page. |
| [filterpipeline.IFixedPage.SetPagePart](nf-filterpipeline-ifixedpage-setpagepart.md) | The SetPagePart method associates a new part with the page. |
| [filterpipeline.IFixedPage.SetPrintTicket](nf-filterpipeline-ifixedpage-setprintticket.md) | The SetPrintTicket method associates a print ticket with the page. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\filterpipeline\nn-filterpipeline-ipartbase.md">IPartBase</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IFixedPage interface%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>