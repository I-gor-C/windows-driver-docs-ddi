---
UID: NN:prcomoem.IPrintCoreHelperUni
title: IPrintCoreHelperUni
author: windows-driver-content
description: This section describes the methods that are defined for the IPrintCoreHelperUni COM interface.
old-location: print\iprintcorehelperuni_interface.htm
old-project: print
ms.assetid: e581d190-8185-45c1-80c7-ff8eb305360e
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintCoreHelperUni, IPrintCoreHelperUni interface [Print Devices], IPrintCoreHelperUni interface [Print Devices], described, prcomoem/IPrintCoreHelperUni, print.iprintcorehelperuni_interface, print_unidrv-pscript_allplugins_ca505d1f-1b52-4a61-a2d8-d8fea10cda76.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
req.include-header: 
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
req.lib: prcomoem.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintCoreHelperUni
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni interface

This section describes the methods that are defined for the <code>IPrintCoreHelperUni</code> COM interface.

## Methods

<p>The <b>IPrintCoreHelperUni</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintCoreHelperUni::CreateDefaultGDLSnapshot](nf-prcomoem-iprintcorehelperuni-createdefaultgdlsnapshot.md) | The IPrintCoreHelperUni::CreateDefaultGDLSnapshot method gets a GDL snapshot based on the driver default configuration. |
| [IPrintCoreHelperUni::CreateGDLSnapshot](nf-prcomoem-iprintcorehelperuni-creategdlsnapshot.md) | The IPrintCoreHelperUni::CreateGDLSnapshot method creates a GDL snapshot of the driver configuration file based on the current configuration. |
| [IPrintCoreHelperUni::CreateInstanceOfMSXMLObject](nf-prcomoem-iprintcorehelperuni-createinstanceofmsxmlobject.md) | The IPrintCoreHelperUni::CreateInstanceOfMSXMLObject method creates an instance of an MSXML object. |
| [IPrintCoreHelperUni::EnumConstrainedOptions](nf-prcomoem-iprintcorehelperuni-enumconstrainedoptions.md) | The IPrintCoreHelperUni::EnumConstrainedOptions method provides a list of all of the options that are constrained in a particular feature, based on current settings. |
| [IPrintCoreHelperUni::EnumFeatures](nf-prcomoem-iprintcorehelperuni-enumfeatures.md) | The IPrintCoreHelperUni::EnumFeatures method gets a list of all available features, including synthesized and core driver-implement features. |
| [IPrintCoreHelperUni::EnumOptions](nf-prcomoem-iprintcorehelperuni-enumoptions.md) | The IPrintCoreHelperUni::EnumOptions method gets a list of available options for the given feature. |
| [IPrintCoreHelperUni::GetFontSubstitution](nf-prcomoem-iprintcorehelperuni-getfontsubstitution.md) | The IPrintCoreHelperUni::GetFontSubstitution method indicates which device font, if any, is used as a substitution font for a specified TrueType font. |
| [IPrintCoreHelperUni::GetOption](nf-prcomoem-iprintcorehelperuni-getoption.md) | The IPrintCoreHelperUni::GetOption method gets a specified option for a given feature. |
| [IPrintCoreHelperUni::SetFontSubstitution](nf-prcomoem-iprintcorehelperuni-setfontsubstitution.md) | The IPrintCoreHelperUni::SetFontSubstitution method specifies the device font to print in place of a given TrueType font. |
| [IPrintCoreHelperUni::SetOptions](nf-prcomoem-iprintcorehelperuni-setoptions.md) | The IPrintCoreHelperUni::SetOptions method sets multiple feature-option pairs at the same time. |
| [IPrintCoreHelperUni::WhyConstrained](nf-prcomoem-iprintcorehelperuni-whyconstrained.md) | The IPrintCoreHelperUni::WhyConstrained method provides a list of options that constrain the specified feature-option pair in the current configuration. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |