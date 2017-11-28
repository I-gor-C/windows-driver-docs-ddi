# Printoem.h header


This header is used by unknown technology.

Printoem.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFNGETINFO callback](nc-printoem-pfngetinfo.md) | The UNIFONTOBJ_GetInfo callback function is provided by the Unidrv driver so that rendering plug-ins can obtain font or glyph information. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [CUSTOMSIZEPARAM structure](ns-printoem--customsizeparam.md) | The CUSTOMSIZEPARAM structure holds information pertaining to a single custom page size parameter for a printer. |
| [DEVOBJ structure](ns-printoem--devobj.md) | The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods. |
| [DEVOBJ structure](ns-printoem--devobj~r1.md) | The DEVOBJ structure is used as an input argument to several of a rendering plug-in's COM interface methods. |
| [DRVPROCS structure](ns-printoem--drvprocs.md) | The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers. |
| [FINVOCATION structure](ns-printoem--finvocation.md) | The FINVOCATION structure is used as input to the IPrintOemUni |
| [GETINFO_FONTOBJ structure](ns-printoem--getinfo-fontobj.md) | The GETINFO_FONTOBJ structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_GLYPHBITMAP structure](ns-printoem--getinfo-glyphbitmap.md) | The GETINFO_GLYPHBITMAP structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_GLYPHSTRING structure](ns-printoem--getinfo-glyphstring.md) | The GETINFO_GLYPHSTRING structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_GLYPHWIDTH structure](ns-printoem--getinfo-glyphwidth.md) | The GETINFO_GLYPHWIDTH structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_MEMORY structure](ns-printoem--getinfo-memory.md) | The GETINFO_MEMORY structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [GETINFO_STDVAR structure](ns-printoem--getinfo-stdvar.md) | The GETINFO_STDVAR structure is used as input to the UNIFONTOBJ_GetInfo callback function. |
| [OEMCUIPPARAM structure](ns-printoem--oemcuipparam.md) | The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI |
| [OEMCUIPPARAM structure](ns-printoem--oemcuipparam~r1.md) | The OEMCUIPPARAM structure is used as an input parameter to a user interface plug-in's IPrintOemUI |
| [OEMDMPARAM structure](ns-printoem--oemdmparam.md) | The OEMDMPARAM structure is used as an input parameter to the IPrintOemUI |
| [OEMUIOBJ structure](ns-printoem--oemuiobj.md) | The OEMUIOBJ structure is used as an input argument to several of the methods exported by user interface plug-ins. |
| [OEMUIPROCS structure](ns-printoem--oemuiprocs.md) | The OEMUIPROCS structure is obsolete.The OEMUIPROCS structure contains the address of the DrvGetDriverSetting and DrvUpdateUISetting functions that are exported by Microsoft printer drivers. |
| [OEMUIPSPARAM structure](ns-printoem--oemuipsparam.md) | The OEMUIPSPARAM structure is passed to a user interface plug-in's IPrintOemUI |
| [OEM_DMEXTRAHEADER structure](ns-printoem--oem-dmextraheader.md) | The OEM_DMEXTRAHEADER structure must be used to define the first members of a set of private DEVMODEW structure members. |
| [PDEV_ADJUST_GRAPHICS_RESOLUTION structure](ns-printoem--pdev-adjust-graphics-resolution.md) | The PDEV_ADJUST_GRAPHICS_RESOLUTION structure specifies a graphics resolution value. |
| [PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure](ns-printoem--pdev-adjust-imageable-origin-area.md) | The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure specifies the imageable origin area. |
| [PDEV_ADJUST_PAPER_MARGIN structure](ns-printoem--pdev-adjust-paper-margin.md) | The PDEV_ADJUST_PAPER_MARGIN structure specifies the imageable printing area. |
| [PDEV_ADJUST_PHYSICAL_PAPER_SIZE structure](ns-printoem--pdev-adjust-physical-paper-size.md) | The PDEV_ADJUST_PAPER_PHYSICAL_SIZE structure specifies a paper size value. |
| [PDEV_HOSTFONT_ENABLED structure](ns-printoem--pdev-hostfont-enabled.md) | The PDEV_HOSTFONT_ENABLED structure indicates whether the Hostfont feature is enabled. |
| [PDEV_USE_TRUE_COLOR structure](ns-printoem--pdev-use-true-color.md) | The PDEV_USE_TRUE_COLOR structure indicates whether the output color space should be color or grayscale. |
| [PIPPARAMS structure](ns-printoem-pipparams.md) | The IPPARAMS structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [POEMMEMORYUSAGE structure](ns-printoem-poemmemoryusage.md) | The OEMMEMORYUSAGE structure is used as an input parameter to a rendering plug-in's IPrintOemUni |
| [PSCRIPT5_PRIVATE_DEVMODE structure](ns-printoem--pscript5-private-devmode.md) | The PSCRIPT5_PRIVATE_DEVMODE structure enables Pscript5 plug-ins to determine the size of the private portion of Pscript5's DEVMODEW structure. |
| [PUBLISHERINFO structure](ns-printoem--publisherinfo.md) | The PUBLISHERINFO structure is used as an input parameter to the IPrintOemPS |
| [SIMULATE_CAPS_1 structure](ns-printoem--simulate-caps-1.md) | The SIMULATE_CAPS_1 structure contains information about the types of simulations a spooler supports. |
| [UNIDRV_PRIVATE_DEVMODE structure](ns-printoem--unidrv-private-devmode.md) | The UNIDRV_PRIVATE_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure. |
| [UNIFONTOBJ structure](ns-printoem--unifontobj.md) | The UNIFONTOBJ structure is used as an input parameter to font functions in rendering plug-ins. |
| [USERDATA structure](ns-printoem--userdata.md) | The USERDATA structure is used by Unidrv and Pscript to specify additional information about printer features. A USERDATA structure pointer is supplied as the UserData member for each OPTITEM structure. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [EATTRIBUTE_DATATYPE enumeration](ne-printoem--eattribute-datatype.md) | The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute. |
| [STDVARIABLEINDEX enumeration](ne-printoem--stdvariableindex.md) | . |
