---
UID: NN:prcomoem.IPrintCoreHelper
title: IPrintCoreHelper
author: windows-driver-content
description: This section describes the methods that are defined for the IPrintCoreHelper COM interface.
old-location: print\iprintcorehelper_interface.htm
old-project: print
ms.assetid: db13410f-e4cb-4077-bb4b-7963e97b435c
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintCoreHelper, IPrintCoreHelper interface [Print Devices], IPrintCoreHelper interface [Print Devices], described, prcomoem/IPrintCoreHelper, print.iprintcorehelper_interface, print_unidrv-pscript_allplugins_9609acef-24e8-4802-9c70-196fef2b011f.xml
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
req.lib: 
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
-	IPrintCoreHelper
product:
- Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintCoreHelper interface

This section describes the methods that are defined for the <b>IPrintCoreHelper</b> COM interface.

## Methods

<p>The <b>IPrintCoreHelper</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintCoreHelper::CreateInstanceOfMSXMLObject](nf-prcomoem-iprintcorehelper-createinstanceofmsxmlobject.md) | The IPrintCoreHelper::CreateInstanceOfMSXMLObject method creates an instance of an MSXML 6.0 object by using the correct MSXML DLL. |
| [IPrintCoreHelper::EnumConstrainedOptions](nf-prcomoem-iprintcorehelper-enumconstrainedoptions.md) | The IPrintCoreHelper::EnumConstrainedOptions method provides a list of all of the options that are constrained in a particular feature, based on current settings. |
| [IPrintCoreHelper::EnumFeatures](nf-prcomoem-iprintcorehelper-enumfeatures.md) | The IPrintCoreHelper::EnumFeatures method gets a list of all available features, including synthesized and core driver-implement features. |
| [IPrintCoreHelper::EnumOptions](nf-prcomoem-iprintcorehelper-enumoptions.md) | The IPrintCoreHelper::EnumOptions method gets a list of available options for the given feature. |
| [IPrintCoreHelper::GetFontSubstitution](nf-prcomoem-iprintcorehelper-getfontsubstitution.md) | The IPrintCoreHelper::GetFontSubstitution method indicates which device font, if any, is used as a substitution font for a specified TrueType font. |
| [IPrintCoreHelper::GetOption](nf-prcomoem-iprintcorehelper-getoption.md) | The IPrintCoreHelper::GetOption method gets a specified option for a given feature. |
| [IPrintCoreHelper::SetFontSubstitution](nf-prcomoem-iprintcorehelper-setfontsubstitution.md) | The IPrintCoreHelper::SetFontSubstitution method specifies the device font to print in place of a given TrueType font. |
| [IPrintCoreHelper::SetOptions](nf-prcomoem-iprintcorehelper-setoptions.md) | The IPrintCoreHelper::SetOptions method sets multiple feature-option pairs at the same time. |
| [IPrintCoreHelper::WhyConstrained](nf-prcomoem-iprintcorehelper-whyconstrained.md) | The IPrintCoreHelper::WhyConstrained method provides a list of options that are constraining the specified feature-option pair in the current configuration. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |