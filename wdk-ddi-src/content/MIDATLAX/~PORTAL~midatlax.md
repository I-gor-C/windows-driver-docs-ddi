# Declarations in the midatlax header
This header Midatlax contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [RxAssociateContextWithMid function](nf-midatlax-rxassociatecontextwithmid.md) | RxAssociateContextWithMid associates the supplied opaque context with an available multiplex ID (MID) from a MID_ATLAS. |
| [RxGetMaximumNumberOfMids function](nf-midatlax-rxgetmaximumnumberofmids.md) | TBD |
| [RxGetNumberOfMidsInUse function](nf-midatlax-rxgetnumberofmidsinuse.md) | TBD |
| [RxCreateMidAtlas function](nf-midatlax-rxcreatemidatlas.md) | RxCreateMidAtlas allocates a new instance of MID_ATLAS data structure and initializes it. |
| [RxMapMidToContext function](nf-midatlax-rxmapmidtocontext.md) | RxMapMidToContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure. |
| [RxReassociateMid function](nf-midatlax-rxreassociatemid.md) | RxReassociateMid reassociates a Multiplex ID (MID) with an alternate context. |
| [RxDestroyMidAtlas function](nf-midatlax-rxdestroymidatlas.md) | RxDestroyMidAtlas destroys an existing instance of a MID_ATLAS data structure and frees the allocated memory. |
| [RxMapAndDissociateMidFromContext function](nf-midatlax-rxmapanddissociatemidfromcontext.md) | RxMapAndDissociateMidFromContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure and then disassociates the MID from the context. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [MID_MAP_ structure](ns-midatlax--mid-map-.md) | TBD |
| [RX_MID_ATLAS structure](ns-midatlax--rx-mid-atlas.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PCONTEXT_DESTRUCTOR callback function](nc-midatlax-pcontext-destructor.md) | TBD |

This header is used in these topics:

- [ifsk](..content/_ifsk)
