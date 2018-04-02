---
UID: NN:filterpipeline.IPartThumbnail
title: IPartThumbnail
author: windows-driver-content
description: The IPartThumbnail interface is an abstraction for thumbnails in an XPS document.
old-location: print\ipartthumbnail.htm
old-project: print
ms.assetid: 2a651a3b-1a5b-4186-9cab-38d9055b8944
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPartThumbnail, IPartThumbnail interface [Print Devices], IPartThumbnail interface [Print Devices], described, filterpipeline/IPartThumbnail, filterpipeline_56710e0f-b3df-44e6-85a5-bd155284531f.xml, print.ipartthumbnail
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
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
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	filterpipeline.h
api_name:
-	IPartThumbnail
product:
- Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPartThumbnail interface

The <b>IPartThumbnail</b> interface is an abstraction for thumbnails in an XPS document.

## Methods

<p>The <b>IPartThumbnail</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPartThumbnail::GetThumbnailProperties](nf-filterpipeline-ipartthumbnail-getthumbnailproperties.md) | The GetThumbnailProperties method gets the thumbnail properties. |
| [IPartThumbnail::SetThumbnailContent](nf-filterpipeline-ipartthumbnail-setthumbnailcontent.md) | The SetThumbnailContent method sets the thumbnail content for the part. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551846">IPartBase</a>